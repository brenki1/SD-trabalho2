from config import db
from flask import abort, make_response
from models import Instrument, instruments_schema, instrument_schema


def read_all(tipo=None, marca=None, condicao=None, min_preco=None, max_preco=None, cordas=None):
    query = Instrument.query

    if tipo: query = query.filter(Instrument.tipo == tipo)
    if marca: query = query.filter(Instrument.marca == marca)
    if condicao: query = query.filter(Instrument.condicao == condicao)
    if cordas: query = query.filter(Instrument.cordas == cordas)
    if min_preco: query = query.filter(Instrument.preco >= min_preco)
    if max_preco: query = query.filter(Instrument.preco <= max_preco)

    instruments = query.all()
    return instruments_schema.dump(instruments)


def create(instrument):
    tipo = instrument.get("tipo")
    cordas = instrument.get("cordas")

    if tipo == "Guitarra" and not (6 <= cordas <= 8):
        abort(400, "Guitarras devem ter entre 6 e 8 cordas.")
    elif tipo == "Contrabaixo" and not (4 <= cordas <= 6):
        abort(400, "Contrabaixos devem ter entre 4 e 6 cordas.")
    elif tipo not in ["Guitarra", "Contrabaixo"]:
        abort(400, "Tipo de instrumento inválido.")

    new_instrument = instrument_schema.load(instrument, session=db.session)
    db.session.add(new_instrument)
    db.session.commit()

    return instrument_schema.dump(new_instrument), 201

def delete(id):
    instrument = Instrument.query.filter(Instrument.id == id).one_or_none()

    if instrument is not None:
        db.session.delete(instrument)
        db.session.commit()
        return make_response(f"Instrumento {id} comprado com sucesso", 200)
    else:
        abort(404, f"Instrumento com ID {id} não encontrado")

def update(id, instrument):
    existing_instrument = Instrument.query.filter(Instrument.id == id).one_or_none()

    if existing_instrument:
        tipo = instrument.get("tipo")
        cordas = instrument.get("cordas")

        if tipo == "Guitarra" and not (6 <= cordas <= 8):
            abort(400, "Guitarras devem ter entre 6 e 8 cordas.")
        elif tipo == "Contrabaixo" and not (4 <= cordas <= 6):
            abort(400, "Contrabaixos devem ter entre 4 e 6 cordas.")
        elif tipo not in ["Guitarra", "Contrabaixo"]:
            abort(400, "Tipo de instrumento inválido.")

        existing_instrument.tipo = tipo
        existing_instrument.marca = instrument.get("marca")
        existing_instrument.cordas = cordas
        existing_instrument.preco = instrument.get("preco")
        existing_instrument.condicao = instrument.get("condicao")
        existing_instrument.imagem_url = instrument.get("imagem_url")

        db.session.commit()
        return instrument_schema.dump(existing_instrument), 200
    else:
        abort(404, f"Instrumento com ID {id} não encontrado")