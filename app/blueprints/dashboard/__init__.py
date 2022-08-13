from flask import Blueprint

blue_dashboard = Blueprint('blue_dashboard', __name__, template_folder='templates')

from .routes import b_dashboard