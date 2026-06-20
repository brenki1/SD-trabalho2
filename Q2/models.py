from datetime import datetime
from config import db, ma


class Instrument(db.Model):
    __tablename__ = "instrument"

    id = db.Column(db.Integer, primary_key=True)
    tipo = db.Column(db.String(32), nullable=False)  # 'Guitarra' ou 'Contrabaixo'
    marca = db.Column(db.String(64), nullable=False)
    cordas = db.Column(db.Integer, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    condicao = db.Column(db.String(32), nullable=False)  # 'Novo' ou 'Usado'
    imagem_url = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class InstrumentSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Instrument
        load_instance = True
        sqla_session = db.session


instrument_schema = InstrumentSchema()
instruments_schema = InstrumentSchema(many=True)