from flask import Blueprint

blue_home = Blueprint('home', __name__, template_folder='templates')

from .routes import route_home