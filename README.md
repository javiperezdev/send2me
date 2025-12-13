📡 send2me
==========

> **The "LAN AirDrop" for everyone.** A self-hosted, secure, and lightning-fast file transfer tool designed to bridge the gap between mobile devices and desktop computers without relying on the cloud.

* * * * *

<br>
<p align="center">
  <strong>📸 Project Preview</strong>
</p>

<p align="center">
  <table>
    <tr>
      <td align="center" width="40%">
        <img src="assets/mobile_preview.png" alt="Vista Móvil - Escaneo QR" width="100%">
        <br>
        <sub>📱 1. Scan from your mobile</sub>
      </td>
      <td align="center" width="60%">
        <img src="assets/desktop_preview.png" alt="Vista Escritorio - Drag & Drop" width="100%">
        <br>
        <sub>💻 2. Receive to your desktop</sub>
      </td>
    </tr>
  </table>
</p>
<br>

📖 Overview
-----------

**send2me** is a lightweight, local web server that allows users to instantly send files from a smartphone (or any other device) to a host computer over a shared Wi-Fi network.

I built this project to solve a common pain point: **Getting a file from Phone to Computer without logging into email, using slow Bluetooth, or compressing quality via messaging apps indeed wasting time.**

Unlike cloud solutions, `send2me` keeps data strictly within the local network (LAN), ensuring privacy, speed, and security.

### ⚡ Key Features

-   **Zero-Config Connection**: Automatically detects the host's local IP and generates a **QR Code** for instant mobile connection.

-   **Drag & Drop Interface**: A modern, responsive frontend that supports drag-and-drop file uploads.

-   **Security First**: Implements **Magic Number validation** (via `filetype` library) to verify true file MIME types, rejecting malicious binaries disguised with fake extensions.

-   **Async Performance**: Built on **FastAPI** to handle concurrent requests efficiently using Python's `async/await` syntax.

-   **User Friendly**: Just downloadin the `.exe` file and following the guideline from [releases](https://github.com/javiperezdev/send2me/releases).


* * * * *

🛠️ Tech Stack
--------------

### Backend

-   **Language**: Python 3.10+

-   **Framework**: [FastAPI](https://fastapi.tiangolo.com/).

-   **Server**: Uvicorn (ASGI).

-   **Image Processing**: `qrcode` (for connection generation) and `Pillow`.

-   **File Validation**: `filetype` (for the signature detection of not allowed files that may be dangerous).

### Frontend

-   **Templating**: Jinja2 (Server-side rendering).

-   **Styling**: Vanilla CSS3 (Custom properties, Flexbox, responsive design).

-   **Logic**: Vanilla JavaScript (Event delegation, Drag & Drop API).

* * * * *

🏗️ System Architecture
-----------------------

The application follows a modular "Router" pattern to maintain clean separation of concerns:

```
src/
├── main.py              # Application entry point & static mounts
├── utils.py              # Utilities
├── routers/
│   ├── conection.py     # Network discovery & QR code generation
│   ├── uploading.py     # File validation logic & disk I/O
│   └── web.py           # HTML template rendering endpoints
├── templates/           # Jinja2 HTML templates
└── static/              # CSS & JS assets

```

### Security Highlight: Magic Number Validation

Instead of trusting file extensions (which can be easily spoofed), `send2me` reads the first 2048 bytes of the file buffer to determine its true hex signature.

-   **Code**: [See `routers/uploading.py`]

-   **Benefit**: Prevents a user from uploading a `.exe` renamed as `.jpg`.

* * * * *

🔮 Future Roadmap
-----------------

-   [ ] **End-to-End Encryption**: Implement HTTPS with self-signed cert generation for public Wi-Fi safety.

-   [x] **Making it more user friendly**: Giving an `.exe` file with all installed, so it becomes a user friendly tool  

-   [ ] **Making it cross platform**: Allow Windows and Mac users, having their  `.exe`.

* * * * *

👨‍💻 Author
------------

**Javiperezdev**

-   **LinkedIn**: [[Link to your LinkedIn](https://es.linkedin.com/in/francisco-javier-p%C3%A9rez-pastor-544830385)]

* * * * *

*Built with ❤️ and Python.*
