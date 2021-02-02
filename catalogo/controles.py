from catalogo import catalogo_bp
from catalogo.dados import listar_cursos_ativos, obter_curso
from flask import render_template



@catalogo_bp.route('/')
def index():
    return render_template(
        'index.html',
        cursos=listar_cursos_ativos()
    )

@catalogo_bp.route('/curso/<slug>')
def curso(slug):
    return render_template(
        'curso.html',
        curso=obter_curso(slug)
    )
