from flask import flash, request, session, render_template
from app.views.forms import CommentForm
from app.controllers.queries.querys import comments
from app.controllers.helper import date_format
from flask_login import current_user, login_required

from app.blueprints.dashboard import blue_dashboard

@blue_dashboard.route('/dashboard', methods = ['GET','POST'])
@login_required
def dashboard():
    
    comment_form = CommentForm(request.form)
    
    try:
        if request.method == 'POST' and comment_form.validate():
            from app.controllers.queries.querys import save_comment
            
            user_id = current_user.id
            
            save_comment.post_comment(user_id=user_id,text=comment_form.comment.data)
            
            success_message = 'Nuevo comentario creado!'
            flash(success_message)
            
            
    except :
        flash('Hay un problema en la publicación del comentario!')    
    
    return render_template('dashboard.html', usuario = current_user.username, form = comment_form,comments = comments.get_comment(), date_format = date_format)

