import os
import platform
import subprocess

def open_img(file_name: str):
    system = platform.system()

    if system == "Windows":
        os.startfile(file_name)
    elif system == "Darwin":
        subprocess.run(["open", file_name], check=True)
    else:
        subprocess.run(["xdg-open", file_name], check=True)