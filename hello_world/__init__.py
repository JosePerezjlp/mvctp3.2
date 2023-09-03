from flask import Flask
from config import Config
from .routes.bikesbp import bikesbp

def inicializar_app():
    """Crea y configura la aplicación Flask"""
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(bikesbp)
    return app