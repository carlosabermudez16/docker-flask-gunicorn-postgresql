
from app.controllers.queries.querys import comments
from flask import jsonify,render_template
from app.controllers.api import blue_api

@blue_api.route('/', defaults = {'path': ''})
@blue_api.route('/<path:path>')
def render_vue(path):
    return render_template("index.html")

@blue_api.route('/services_api_public/v1/publications',methods = ['GET'])
def api_publication():
    
    datos = comments.get_comment()
    lista = []
    for data in datos:
        dic = {}
        dic['date'] = data.created_date
        dic['name'] = data.username
        dic['text'] = data.text
        lista.append(dic)
    
    return jsonify({'data':lista})




 
 