import shutil
import filetype
import os
from pathlib import Path
from fastapi import APIRouter, HTTPException, File, UploadFile, Request
from fastapi.templating import Jinja2Templates
from routers.conection import get_local_ip


router = APIRouter()

def get_downloads_folder():
    return Path.home() / "Downloads"

async def validate_file(file: UploadFile = File(...)):
     # List A: Only binary files (with digital signature)
    ALLOWED_BINARY_MIMES = {
        "image/jpeg",
        "image/png",
        "image/gif",
        "image/webp",
        "application/pdf",
        "application/zip",
        "application/x-rar-compressed"
    }

    # List B: text files or code (without digital signature)
    ALLOWED_TEXT_EXTENSIONS = {
        ".txt", ".md", ".csv", ".json", ".xml", ".html", ".css", ".js", 
        ".py", ".java", ".c", ".cpp", ".h", ".sql", ".log"
    }

    header = await file.read(2048)
    await file.seek(0)
    
    kind = filetype.guess(header)

    if kind is not None:
        if kind.mime in ALLOWED_BINARY_MIMES:
            return True 
        else:
            raise HTTPException(400, f"Dangerous binary file detected: {kind.mime}")

    else:
        filename = file.filename.lower()
        _, ext = os.path.splitext(filename) 
        
        if ext in ALLOWED_TEXT_EXTENSIONS:
            return True
        else:
            raise HTTPException(400, f"file extension not allowed: {ext}")

@router.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):

    base_folder = get_downloads_folder()
    base_folder.mkdir(exist_ok=True)
    
    destination_path = base_folder / file.filename
    
    await validate_file(file)   
    templates = Jinja2Templates(directory="templates") 

    try:
        with open(destination_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        return templates.TemplateResponse("upload.html", {
            "request" : request,
            "message" : "File was succesfully shared, it is located in your download directory",
            "type" : "succes",
            "server_ip" : get_local_ip()
        } )
    
    except Exception as e: 
        return templates.TemplateResponse("upload.html", {
            "request" : request,
            "message" : "File was not uploaded, please try again later!",
            "type" : "error",
            "server_ip" : get_local_ip()
        } )
    
