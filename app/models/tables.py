from app import db


class Convidados(db.Model):
    __tablename__ = "convidados"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(40), unique=True)
    numero_convidados = db.Column(db.Integer)
    confirmou_presenca = db.Column(db.DateTime)
    fk_noivo = db.Column(db.Integer, db.ForeignKey('noivos.id'), unique=True)

    noivo = db.relationship('Noivos', uselist=False, foreign_keys=fk_noivo)


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
    preco = db.Column(db.Float(10, 2))

    referencias = db.relationship('ReferenciaPresente', backref='presente')


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
