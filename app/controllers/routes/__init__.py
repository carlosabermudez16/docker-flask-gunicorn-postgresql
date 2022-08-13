from flask import Blueprint

bp_rutas_all = Blueprint('routes_all', __name__,
                    template_folder = 'templates')

from . import rutas