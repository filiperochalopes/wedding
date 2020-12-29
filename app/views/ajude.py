from flask import render_template
from app import app

@app.route("/ajude")
def ajude():
    return render_template('ajude.html')