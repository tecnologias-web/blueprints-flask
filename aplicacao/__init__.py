from flask import Flask
from catalogo import catalogo_bp


app = Flask('aplicacao')
app.config.from_object('aplicacao.config.Configuracao')


app.register_blueprint(catalogo_bp)