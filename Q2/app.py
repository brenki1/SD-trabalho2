from flask import render_template, request
import config
from models import Instrument

app = config.connex_app
app.add_api(config.basedir / "swagger.yml")

@app.route("/")
def home():
    query = Instrument.query

    tipo = request.args.get('tipo')
    marca = request.args.get('marca')
    condicao = request.args.get('condicao')

    if tipo: query = query.filter(Instrument.tipo == tipo)
    if marca: query = query.filter(Instrument.marca == marca)
    if condicao: query = query.filter(Instrument.condicao == condicao)

    instruments = query.all()
    return render_template("home.html", instruments=instruments)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)