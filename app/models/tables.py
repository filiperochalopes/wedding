from app import db


class Convidados(db.Model):
    __tablename__= "convidados"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    numero_convidados = db.Column(db.Integer)
    confirmou_presenca = db.Column(db.DateTime)
    fk_noivo = db.Column(db.Integer, db.ForeignKey('fk_noivo') unique=True)

    convidados = db.relationship('Noivos', foreign_keys=fk_noivo)

class Noivos(db.Model):
    __tablename__ = "noivos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(80), unique=True)
    senha = db.Column(db.String(128))

    
class Presente(db.Model):
    __tablename__ = "presentes"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(128))
    imagem = db.Column(db.String(128))
    price = db.Column(db.Float(10,2))


class Referencia_presentes(db.Model):
    __tablename__ = "referencia_presentes"

    id = db.Column(db.Integer, primary_key=True)
    link_referencia = db.Column(db.Texto)
    fk_presente = db.Column(db.Integer,db.ForeignKey('fk_presente'))

    referencias = db.relationship('Presentes', foreign_keys=fk_presente)


    
class Presentes_comprados(db.Model):
    __tablename__ = "presentes_comprados"

    id = db.Column(db.Integer, primary_key-True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(60))
    fk_presente = db.Column(db.Integer,db.ForeignKey('fk_presente'))
    mensagem = db.Column(db.Text)
    id_transacao = db.Column(db.String(128))

    comprados = db.relationship('Presentes', foreign_keys=fk_presente)


class Doacoes(db.Model):
    __tablename__=doaçoes

    id = db.Column(db.Integer, primary_key-True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(60))
    valor = db.Column(db.Float)
    mensagem = db.Column(db.Text)
    id_transacao = db.Column(db.String(128))


class mensagens(db.Model):
    __tablename__= mensagens

    id = db.Column(db.Integer, primary_key-True)
    nome = db.Column(db.String(40))
    email = db.Column(db.String(60))
    mensagem = db.Column(db.Text)