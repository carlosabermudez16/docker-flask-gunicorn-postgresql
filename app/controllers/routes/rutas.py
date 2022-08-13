from app.controllers.routes import bp_rutas_all

from flask import render_template

@bp_rutas_all.route('/', defaults = {'path': ''})
@bp_rutas_all.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")


#"""-------------- RUTAS PÚBLICAS --------------"""
#
#"""Registro de las rutas blueprint del home"""
#from app.blueprints.home import blue_home
#bp_rutas_all.register_blueprint(blue_home)
#
#"""Registro de las rutas blueprint de las apis"""
#from app.controllers.api.apis import blue_api
#bp_rutas_all.register_blueprint(blue_api)
#
#"""Registro de las rutas blueprint de registro y login"""
#from app.blueprints.auth import blue_rg
#bp_rutas_all.register_blueprint(blue_rg)
#
#"""-------------- RUTAS CON INICIO DE SESIÓN --------------"""
#
#"""Registro de las rutas blueprint de la dashboard"""
#from app.blueprints.dashboard import blue_dashboard
#bp_rutas_all.register_blueprint(blue_dashboard)
#
#"""Registro de ruta de publicaciones"""
#from app.blueprints.publication import blue_comments
#bp_rutas_all.register_blueprint(blue_comments)







