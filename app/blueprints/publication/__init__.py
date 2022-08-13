from flask import Blueprint

blue_comments = Blueprint('b_c', __name__, template_folder='templates')

from .routes import b_comment