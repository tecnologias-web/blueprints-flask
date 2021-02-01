from catalogo import catalogo_bp
from flask import render_template


@catalogo_bp.route('/')
def index():
    return render_template('index.html')