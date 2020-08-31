from app import app
from io import BytesIO
import pyperclip

@app.route("/copy_to_clipboard_convite/{id}", methods=["GET"])
def copy_to_clipboard_convite():
    pyperclip.copy('The text to be copied to the clipboard.')