from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from routers.conection import get_local_ip
from fastapi.responses import HTMLResponse
from utils import resource_path


router = APIRouter(tags=["web"])
templates = Jinja2Templates(directory=resource_path("templates"))



@router.get("/upload_web", response_class=HTMLResponse)
async def page_to_show(request: Request):
    return templates.TemplateResponse("upload.html", {"request" : request, "server_ip" : get_local_ip()})
    
@router.get("/qr_web", response_class=HTMLResponse)
async def page_to_show(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request, "host_url" : get_local_ip()})
    

    
