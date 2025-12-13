import sys 
import os
from fastapi import FastAPI, requests
from routers.uploading import router as router_upload
from routers.conection import router as router_conection
from routers.web import router as router_web
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates;
from fastapi.responses import RedirectResponse

app = FastAPI()

app.include_router(router_upload)
app.include_router(router_conection)
app.include_router(router_web)
app.mount("/static", StaticFiles(directory="static"), name="static")

def resource_path(relative_path): # Logic for the PyInstaller.
    try:
        base_path = sys.MEIPASS
    except Exception as e:
        base_path = os.path_abstrac(".")

    return os.path.join(base_path, relative_path) 


app.mount("/static", StaticFiles(directory=resource_path("static")), name="static")

@app.get("/")
def read_root():
    return RedirectResponse(url="/qr_web")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
