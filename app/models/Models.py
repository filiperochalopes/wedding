from app import db
from sqlalchemy.dialects.mysql.base import MSBinary
import uuid

def generate_uuid():
    return str(uuid.uuid4())

class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)


class Convidado(db.Model):
    __tablename__ = "convidados"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    numero_convidados = db.Column(db.Integer)
    confirmou_presenca_timestamp = db.Column(db.DateTime)
    confirmou_presenca_numero = db.Column(db.Integer)
    negou_presenca = db.Column(db.Boolean, default=False)
    pendencia = db.Column(db.Boolean, default=False)
    pendencia_texto = db.Column(db.Text, default=None)
    convite_uuid = db.Column(db.String(64), default=generate_uuid)
    fk_noivo = db.Column(db.Integer, db.ForeignKey('noivos.id'), )
    fk_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'))

    noivo = db.relationship('Noivo', uselist=False, foreign_keys=fk_noivo, lazy="selectin")
    categoria = db.relationship('Categoria', uselist=False, foreign_keys=fk_categoria, lazy="selectin")

    def __repr__(self):
        return "<Convidado(nome='%s')>" % (self.nome)


class Noivo(db.Model):
    __tablename__ = "noivos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(80), unique=True)
    senha = db.Column(db.String(128))


class Presente(db.Model):
    __tablename__ = "presentes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    imagem = db.Column(db.String(512))
    preco = db.Column(db.Float(10, 2))
    fk_categoria = db.Column(db.Integer, db.ForeignKey('categorias.id'))

    referencias = db.relationship('ReferenciaPresente', backref='presente')
    categoria = db.relationship('Categoria', uselist=False, foreign_keys=fk_categoria, lazy="selectin")


class ReferenciaPresente(db.Model):
    __tablename__ = "referencia_presentes"

    id = db.Column(db.Integer, primary_key=True)
    link_referencia = db.Column(db.Text)
    fk_presente = db.Column(db.Integer, db.ForeignKey('presentes.id'))


class PresentesComprado(db.Model):
    __tablename__ = "presentes_comprados"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(60))
    fk_presente = db.Column(db.Integer, db.ForeignKey('presentes.id'))
    mensagem = db.Column(db.Text)
    id_transacao = db.Column(db.String(128))

    presente = db.relationship(
        'Presente',
        uselist=False,
        foreign_keys=[fk_presente])


class Doacoes(db.Model):
    __tablename__ = "doacoes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(60))
    valor = db.Column(db.Float)
    mensagem = db.Column(db.Text)
    id_transacao = db.Column(db.String(128))


class Mensagens(db.Model):
    __tablename__ = "mensagens"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(60))
    mensagem = db.Column(db.Text)


class Configuracoes(db.Model):
    __tablename__ = "configuracoes"

    id = db.Column(db.Integer, primary_key=True)
    chave = db.Column(db.String(40))
    valor = db.Column(db.String(64))