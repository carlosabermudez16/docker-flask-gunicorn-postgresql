from flask import Blueprint

blue_rg = Blueprint('rg', __name__, template_folder='templates')

from .routes import rb_lr