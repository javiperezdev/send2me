import socket
import io
import qrcode
from fastapi import APIRouter
from fastapi.responses import StreamingResponse


router = APIRouter()
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
        s.close()
        return local_ip
    except Exception:
        return "127.0.0.1"


@router.get("/qr")
def get_qr_code():
    my_ip = get_local_ip()
    url_to_share = f"http://{my_ip}:8000/upload_web"
    

    qr_image = qrcode.make(url_to_share)
    buffer = io.BytesIO()
    qr_image.save(buffer, format="PNG")
    buffer.seek(0)
    
    return StreamingResponse(buffer, media_type="image/png")
