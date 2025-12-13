import sys
import os
import socket
from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from routers.conection import get_local_ip
from fastapi.responses import HTMLResponse

def resource_path(relative_path): # Logic for the PyInstaller.
    try:
        base_path = sys.MEIPASS
    except Exception as e:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, "..", relative_path) 

router = APIRouter(tags=["web"])
templates = Jinja2Templates(directory=resource_path("templates"))



@router.get("/upload_web", response_class=HTMLResponse)
async def page_to_show(request: Request):
    return templates.TemplateResponse("upload.html", {"request" : request, "server_ip" : get_local_ip()})
    
@router.get("/qr_web", response_class=HTMLResponse)
async def page_to_show(request: Request):
    return templates.TemplateResponse("index.html", {"request" : request, "host_url" : get_local_ip()})
    

    
