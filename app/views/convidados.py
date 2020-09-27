from flask import render_template
from app import app, db

from app.models.Models import Convidados

@app.route("/convidados")
def convidados():
    convidados = db.session.query(Convidados).all()
    return render_template('convidados.html', convidados=convidados)

@app.route("/convite/<uuid>")
def convite(uuid):
    print(uuid)
    convidado = db.session.query(Convidados).filter(Convidados.convite_uuid == uuid).one()
    return render_template('convite.html', convidado=convidado)