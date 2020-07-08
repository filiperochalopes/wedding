from flask import render_template, jsonify
from app import app, db
import json

from app.models.forms import LoginForm
from app.models.tables import Convidados


@app.route("/hello_world")
def hollo_world():
    return "Hello World"


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/convidados")
def convidados():
    convidados = db.session.query(Convidados).all()
    for c in convidados:
        print(c.__dict__)
    return render_template('convidados.html', convidados=convidados)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        print(form.username.data)
        print(form.password.data)
    else:
        print(form.errors)
    return render_template('login.html',
                           form=form)

# @app.route("/visualizar_presentes")
# def view_gift():
#      gifts = db.session.query(Gift).all()
#      print(gifts)
#      return render_template('presentes.html', gifts=gifts)
