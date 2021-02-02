from flask import Flask
from admin import admin_bp
from catalogo import catalogo_bp


app = Flask('aplicacao')
app.config.from_object('aplicacao.config.Configuracao')

app.register_blueprint(catalogo_bp)
app.register_blueprint(admin_bp, url_prefix='/admin')