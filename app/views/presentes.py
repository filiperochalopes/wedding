from flask import render_template
from app import app, db

from app.models.Models import Presente

@app.route("/presentes")
def presentes():
    presentes = db.session.query(Presente).all()
    print(presentes)
    return render_template('presentes.html', presentes=presentes)