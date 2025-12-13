import os 
import sys

def resource_path(relative_path): # Logic for the PyInstaller.
    try:
        base_path = sys.MEIPASS
    except Exception as e:
        base_path = os.path.dirname(os.path.abspath(__file__))

    return os.path.join(base_path, relative_path) 

