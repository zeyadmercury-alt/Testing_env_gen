import uvicorn
from src.app import create_app

app = create_app()

@app.get("/debug")
def debug():
    import os, pathlib
    folder = pathlib.Path(__file__).with_name("static")
    return {"static_folder": str(folder), "files": list(folder.glob("*"))}
@app.get("/static-test")
def static_test():
    from pathlib import Path
    file = Path(__file__).with_name("static") / "mercury.css"
    exists = file.exists()
    size   = file.stat().st_size if exists else 0
    return {"file": str(file), "exists": exists, "size_bytes": size}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)