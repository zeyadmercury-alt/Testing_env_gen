from fastapi import FastAPI
from src.routes import pages, api
from fastapi.staticfiles import StaticFiles

def create_app() -> FastAPI:
    app = FastAPI(title="Gen – ComfyUI front-end")
    app.mount("/static", StaticFiles(directory="static"), name="static")
    app.include_router(pages.router)
    app.include_router(api.router)
    return app