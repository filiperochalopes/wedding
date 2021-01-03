from flask import render_template
from app import app, db
from flask import request
from functools import reduce
from pprint import pprint

from app.models.Models import Convidado, Categoria, Noivo

@app.route("/convidados")
def convidados():
    convidados = db.session.query(Convidado).all()
    convidados = sorted(convidados, key=lambda convidado: convidado.nome if convidado.nome else 'z')

    def contar_convidados(convidados):
        return reduce(lambda acc,cur : acc+cur.numero_convidados if cur.numero_convidados else acc, convidados, 0)

    total_convidados = contar_convidados(convidados)
    media_convidados_por_convite = total_convidados / len([convidado for convidado in convidados if convidado.nome is not None])
    estatisticas = {
        'total_convidados': total_convidados,
        'media_convidados_por_convite': media_convidados_por_convite,
        'categorias' : {},
        'noivos': {}
    }

    def estatistica_por_categorias(convidados):
        def reducer_categorias(acc, cur):
            if cur.categoria and cur.categoria.nome:
                if cur.categoria.nome in acc:
                    acc[cur.categoria.nome].append(cur)
                else:
                    acc[cur.categoria.nome] = [cur]
            return acc
        convidados_categorias = reduce(reducer_categorias, convidados, {})
        estatisticas_convidados_categorias = {}
        for nome, lista_convidados in convidados_categorias.items():
            estatisticas_convidados_categorias[nome] = contar_convidados(lista_convidados)
        
        return estatisticas_convidados_categorias

    categorias = db.session.query(Categoria).all()
    categorias_nomes = [categoria.nome for categoria in categorias]
    categorias_ids = [categoria.id for categoria in categorias]
    estatisticas['categorias'] = estatistica_por_categorias(convidados)
    noivos = db.session.query(Noivo).all()
    for noivo in noivos:
        convidados_noivo = db.session.query(Convidado).filter(Convidado.nome is not None, Convidado.fk_noivo == noivo.id).all()
        estatisticas['noivos'][noivo.nome] = {}
        estatisticas['noivos'][noivo.nome]['id'] = noivo.id
        estatisticas['noivos'][noivo.nome]['categorias'] = estatistica_por_categorias(convidados_noivo)
        estatisticas['noivos'][noivo.nome]['total'] = contar_convidados(convidados_noivo)

    pprint(estatisticas)

    return render_template('convidados.html', convidados=convidados, estatisticas=estatisticas)

@app.route("/convite/<uuid>")
def convite(uuid):
    print(uuid)
    convidado = db.session.query(Convidado).filter(Convidado.convite_uuid == uuid).one()
    return render_template('convite.html', convidado=convidado, uuid=uuid)

@app.route("/confirma_presenca", methods=["POST"])
def confirma_presenca():
    uuid = request.form.get('uuid')
    numero_convidados = request.form.get('numero_convidados')
    return f"Hello world {uuid} {numero_convidados}"