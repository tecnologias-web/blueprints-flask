from flask import Blueprint

catalogo_bp = Blueprint(
    'catalogo',
    __name__,
    template_folder='templates'
)

from . import controles
