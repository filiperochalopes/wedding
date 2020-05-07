from flask import render_template, jsonify
from app import app, db
import json

from app.models.tables import User, Gift
from app.models.forms import LoginForm

@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')

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

@app.route("/adicionar_presente/<name>/<price>")
def add_gift(name,price):
    gift = Gift(
        name=name,
        price=price
    )
    db.session.add(gift)
    db.session.commit()
    return {
        "name":name,
        "price":price
    }

@app.route("/visualizar_presentes")
def view_gift():
     gifts = db.session.query(Gift).all()
     print(gifts)
     return render_template('lista_presente.html', gifts=gifts)
