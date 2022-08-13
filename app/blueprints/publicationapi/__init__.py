
from flask import Blueprint

consumo_api = Blueprint('consumo_api', __name__,
                    template_folder = 'templates')

from . import route