from flask import render_template, jsonify
from app import app, db
import json

from app.models.Forms import LoginForm
from app.models.Models import Convidados


@app.route("/hello_world")
def hollo_world():
    return "Hello World"

@app.route("/hello")
def hello():
    '''Apenas uma página de teste que não tenha requisição de banco para teste'''
    return render_template('hello.html')


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
