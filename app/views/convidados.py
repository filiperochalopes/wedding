from flask import render_template
from app import app, db

from app.models.tables import Convidados

@app.route("/convidados")
def convidados():
    convidados = db.session.query(Convidados).all()
    for c in convidados:
        print(c.__dict__)
    return render_template('convidados.html', convidados=convidados)