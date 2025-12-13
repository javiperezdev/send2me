from fastapi import FastAPI, Request
from routers.uploading import router as router_upload
from routers.conection import router as router_conection
from routers.web import router as router_web
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from utils import resource_path

app = FastAPI()

app.include_router(router_upload)
app.include_router(router_conection)
app.include_router(router_web)

app.mount("/static", StaticFiles(directory=resource_path("static")), name="static")

@app.get("/")
def read_root():
    return RedirectResponse(url="/qr_web")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
