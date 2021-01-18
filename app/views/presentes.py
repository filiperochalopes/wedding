from flask import render_template
from app import app, db
from flask import request
import requests

from app.models.Models import Presente

@app.route("/presentes")
def presentes():
    presentes = db.session.query(Presente).order_by(Presente.fk_categoria.asc(), Presente.preco.asc()).all()
    return render_template('presentes.html', presentes=presentes)

@app.route("/processar_pagamento", methods=["POST"])
def processar_pagamento():
    token = request.form.get('token')
    amount = request.form.get('amount')
    api_key_test = "ak_test_D67WtwUuf2dYB4u7N2pPuThmhN1KHY"
    api_key_live = "ak_live_ZtKhKIDkSJa9n6PhvOgVPwD5KEFsBj"

    r = requests.post(f"https://api.pagar.me/1/transactions/{token}/capture", data={
        'amount': amount,
        'api_key': api_key_live
    })

    print(r.status_code)
    print(r.json())
    
    return r.json()