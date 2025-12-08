from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def index(request: Request): return templates.TemplateResponse("index.html", {"request": request})

@router.get("/txt2img", response_class=HTMLResponse)
def hub(request: Request): return templates.TemplateResponse("txt2img.html", {"request": request})

@router.get("/txt2img/api", response_class=HTMLResponse)
def api_page(request: Request): return templates.TemplateResponse("txt2img/api.html", {"request": request})

@router.get("/txt2img/intake2moodboard", response_class=HTMLResponse)
def intake_page(request: Request): return templates.TemplateResponse("txt2img/intake2moodboard.html", {"request": request})

@router.get("/txt2img/localmodel", response_class=HTMLResponse)
def local_page(request: Request): return templates.TemplateResponse("txt2img/localmodel.html", {"request": request})