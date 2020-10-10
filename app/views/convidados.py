from flask import render_template
from app import app, db

from app.models.Models import Convidado

@app.route("/convidados")
def convidados():
    convidados = db.session.query(Convidado).all()
    print(convidados)
    print()
    convidados = sorted(convidados, key=lambda convidado: convidado.nome if convidado.nome else 'z')
    return render_template('convidados.html', convidados=convidados)

@app.route("/convite/<uuid>")
def convite(uuid):
    print(uuid)
    convidado = db.session.query(Convidado).filter(Convidado.convite_uuid == uuid).one()
    return render_template('convite.html', convidado=convidado)