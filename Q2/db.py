from config import app, db
from models import Instrument


def setup_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        instrumentos_teste = [
            Instrument(
                tipo="Guitarra",
                marca="Fender Stratocaster",
                cordas=6,
                preco=8500.00,
                condicao="Novo",
                imagem_url="https://images.unsplash.com/photo-1564186763535-ebb21ef5277f?w=400&q=80"
            ),
            Instrument(
                tipo="Guitarra",
                marca="Ibanez Iron Label",
                cordas=8,
                preco=6200.00,
                condicao="Usado",
                imagem_url="https://images.unsplash.com/photo-1550291652-6cb9117a4771?w=400&q=80"
            ),
            Instrument(
                tipo="Contrabaixo",
                marca="Music Man StingRay",
                cordas=4,
                preco=12500.00,
                condicao="Novo",
                imagem_url="https://images.unsplash.com/photo-1485278537138-4e8911a13c02?w=400&q=80"
            ),
            Instrument(
                tipo="Contrabaixo",
                marca="Yamaha TRBX",
                cordas=5,
                preco=2800.00,
                condicao="Usado",
                imagem_url="https://images.unsplash.com/photo-1514649923863-ceaf75b77000?w=400&q=80"
            )
        ]
        db.session.add_all(instrumentos_teste)
        db.session.commit()

        print("✅ Banco de dados 'marketplace.db' inicializado e populado com SQLAlchemy com sucesso!")


if __name__ == "__main__":
    setup_database()