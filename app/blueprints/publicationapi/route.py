from flask import render_template
from app.blueprints.publicationapi import consumo_api

@consumo_api.route('/', defaults = {'path': ''})
@consumo_api.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")




 
 