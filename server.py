# server.py  –  one-file version, no packages, no src/
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import json, pathlib, asyncio, httpx

app = FastAPI()
COMFY = "http://127.0.0.1:8188"
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

async def comfy_run(wf_file: str, patches: dict) -> list[str]:
    wf = json.loads(pathlib.Path(f"static/workflows/{wf_file}").read_text())
    for node_id, field_val in patches.items():
        for field, value in field_val.items():
            wf[node_id]["inputs"][field] = value
    async with httpx.AsyncClient() as client:
        r = await client.post(f"{COMFY}/prompt", json={"prompt": wf})
        r.raise_for_status()
        pid = r.json()["prompt_id"]
        while True:
            await asyncio.sleep(1)
            hist = (await client.get(f"{COMFY}/history/{pid}")).json()
            if not hist.get(pid, {}).get("outputs"):
                continue
            for node in hist[pid]["outputs"].values():
                if node.get("images"):
                    return [f"{COMFY}/view?filename={i['filename']}&subfolder={i['subfolder']}&type={i['type']}"
                            for i in node["images"]]

@app.get("/", response_class=HTMLResponse)
def index(request: Request): return templates.TemplateResponse("index.html", {"request": request})
@app.get("/txt2img", response_class=HTMLResponse)
def hub(request: Request): return templates.TemplateResponse("txt2img.html", {"request": request})
@app.get("/txt2img/api", response_class=HTMLResponse)
def api_page(request: Request): return templates.TemplateResponse("txt2img/api.html", {"request": request})
@app.get("/txt2img/intake2moodboard", response_class=HTMLResponse)
def intake_page(request: Request): return templates.TemplateResponse("txt2img/intake2moodboard.html", {"request": request})
@app.get("/txt2img/localmodel", response_class=HTMLResponse)
def local_page(request: Request): return templates.TemplateResponse("txt2img/localmodel.html", {"request": request})

@app.post("/txt2img/api")
async def api_gen(prompt: str = Form(...), model: str = Form(...)):
    return {"images": await comfy_run("api.json", {"1": {"STRING": prompt}, "5": {"image_generation_model": model}})}
@app.post("/txt2img/intake2moodboard")
async def intake_gen(prompt: str = Form(...), category: str = Form(...), summary: str = Form(...)):
    return {"images": await comfy_run("intake2moodboard.json", {"23": {"STRING": prompt}, "21": {"STRING": category}, "22": {"STRING": summary}})}
@app.post("/txt2img/localmodel")
async def local_gen(pprompt: str = Form(...), nprompt: str = Form(""), seed: str = Form("randomize"), summary: str = Form(...)):
    return {"images": await comfy_run("localmodel.json", {"23": {"STRING": pprompt}, "24": {"STRING": nprompt}, "25": {"STRING": seed}, "22": {"STRING": summary}})}