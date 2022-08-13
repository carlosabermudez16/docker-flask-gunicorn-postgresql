from flask import render_template, redirect, request
from flask import flash, url_for, make_response
from flask import copy_current_request_context
from flask_login import login_user, logout_user, current_user, login_required
from app.views.forms import CreateForm, LoginForm
import os

from app.controllers.helper import send_email, send_email_restore_pass
from threading import Thread
from werkzeug.urls import url_parse

from app.blueprints.auth import blue_rg
from app.middlewares.middleware import rld_before_request
rld_before_request # --> permite cargar las before request que están creada para estas peticiones

from app.controllers.token import confirm_token
# comfinrmación de correo
@blue_rg.route("/confirm/<token>")
def confirm_email(token):
    email = confirm_token(token)
    if email:
        from app.controllers.queries.querys import query_email
        
        user = query_email.get_email(email=email)
        
        if user.confirmed:
            if current_user.is_authenticated:
                flash('Cuenta ya confirmada y te registraste.')
                return redirect(url_for('blue_dashboard.dashboard'))
            flash('Tu cuenta está lista y confirmada. por favor logueate.', 'success')
            return redirect(url_for('rg.loggin'))
        else:
            from app.controllers.queries.querys import confirmed_register
            
            confirmed_register.confirmed(user=user)
            
            flash('Has confirmado tu cuenta. ¡Gracias!', 'success')
            return redirect(url_for('rg.loggin'))
    else:
        if current_user.is_authenticated:
            return redirect(url_for('rg.unconfirmed'))
        flash('The confirmation link is invalid or has expired. Please login.', 'danger')
        return redirect(url_for('rg.loggin'))

@blue_rg.route('/errorconfirmate')
@login_required
def unconfirmed():
    if current_user.confirmed:
        flash("El token ha sido alterado.")
        return redirect(url_for('home.home'))
    flash("Por favor comfirme su cuenta de correo")
    return render_template('errorconfirmate.html')

import requests, json
def comprobar_humano(respuesta_del_captcha):
    secret = os.getenv("SECRET_RECAPTCHAP")
    payload = {'response':respuesta_del_captcha, 'secret':secret}
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", payload)
    response_text = json.loads(response.text)
    return response_text['success']

@blue_rg.route('/register',methods = ['GET','POST'])
def register():
    create_form = CreateForm(request.form)
    sitekey = os.getenv("SITIKEY") 
    
    if request.method == 'POST' and create_form.validate():
        respuesta_del_captcha = request.form['g-recaptcha-response']
        from app.controllers.queries.querys import save_register
        
        if comprobar_humano(respuesta_del_captcha):
            import uuid
            public_id = str(uuid.uuid4())
            user = save_register.post_register(create_form.username.data,
                                                create_form.password.data,
                                                create_form.email.data,
                                                public_id = public_id
                                                )
           
            # ENVÍO DE CORREO
            @copy_current_request_context
            def send_message(email, username):
                send_email(email, username)

            sender = Thread(name = 'mail_sender', target = send_message,
                            args=(user.email,user.username))
            sender.start()
            # FIN ENVÍO DE CORREO

            #login_user(user, remember=True)
            next_page = request.args.get('next', None)
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('rg.unconfirmed')
                message = f'Usuario creado!, bienvenido a la página... mira tu correo {user.email}'
                flash(message)
        else:
           #Si devuelve False
            status = "Error, vuelve a comprobar que no eres un robot."
            print (status)
            
    else:
        print('No se a diligenciado el formulario')
        
    return render_template('register.html',form = create_form, sitekey=sitekey)

@blue_rg.route('/loggin',methods = ['GET','POST'])
def loggin():
    login_form = LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        
        from app.controllers.queries.querys import save_loggin
        
        username = login_form.username.data
        password = login_form.password.data
        remember = login_form.remember.data
        
        user = save_loggin.post_loggin(username)
        
        if user is None:
            success_message = f'El usuario {username} no se encuentra registrado, va a ser redireccionado al formulario de registro'
            flash(success_message)
            return redirect(url_for('rg.register'))
        elif user is not None and user.verify_password(password) :
            
            # creamos las sesión
            login_user(user, remember=remember)
            
            # mensaje de bienvenida
            next_page = request.args.get('next')
            
            if not next_page or url_parse(next_page).netloc != '':
                next_page = url_for('blue_dashboard.dashboard')
            success_message = f'Bienvenido {username}'
            flash(success_message)
            
            #agregaoms un token en la cookie
            response = make_response(redirect(next_page))
            
            import jwt
            
            token = jwt.encode(payload={'tokens_jwt': user.public_id}, 
                                key= os.getenv("SECRET_KEY"),
                                algorithm="HS256")
            token.encode("UTF-8")
            
            # forma 1 usando cookie
            response.set_cookie('token', token)
            
            # forma 2 usnaod sesión
            #from flask import session
            #session['token'] = token
            
            
            return response
        else:
            error_message = 'Usuario o contraseña no valida'
            flash(error_message)
        
    return render_template('loggin.html', form = login_form)

@blue_rg.route('/logout')
def logout():
    
    logout_user()
    
    # forma 1 usando cookie
    response = make_response(redirect(url_for('rg.loggin')))  
    response.set_cookie('token',value='',expires=0)
    
    # fomra 2 usando session
    #from flask import session
    #if 'token' in session:
    #    session.pop('token')
    
    return response

# Forget the password
from app.views.forms import RestorePassMailForm, RestorePassForm
from app.controllers.queries.querys import query_email
@blue_rg.route("/restore/", methods=["GET", "POST"])
def restore():
    form = RestorePassMailForm(request.form)
    if request.method == "POST" and form.validate():
        user = query_email.get_email(form.email.data)
        
        @copy_current_request_context
        def send_message(email, username):
            send_email_restore_pass(email, username)

        sender = Thread(name = 'mail_sender', target = send_message,
                        args=(user.email, user.username))
        sender.start()
        # FIN ENVÍO DE CORREO
        message = "Revisa tu correo, haz clic para cambiar tu contraseña!"
        
        flash(message)
        return redirect(url_for('rg.loggin'))
    return render_template("restore_pass_form_mail.html", form=form)

from flask import current_app
@blue_rg.route("/confirm_restore_password/<token>")
def confirm_restore_password(token):
    email = confirm_token(token)

    if email:
        
        try:
            user = query_email.get_email(email=email)
            flash("Restaura tu contraseña:")
        except:
            flash("Ha ocurrido un error, por favor intentalo de nuevo.")
            return redirect(url_for("rg.loggin"))
        
        current_app.config['USER_MAIL'] = user.email
        return redirect(url_for('rg.restore_password'))
    else:
        flash('La confirmación del link es invalida o a expirado. Por favor intenta de nuevo.', 'danger')
        return redirect(url_for("rg.loggin"))

@blue_rg.route("/restore_password/", methods=["GET", "POST"])
def restore_password():
    form = RestorePassForm(request.form)
    context = {
        "form": form
    }
    if request.method == 'POST' and form.validate():
        from app.controllers.queries.querys import new_password
        
        email = current_app.config['USER_MAIL']
        password = form.confirm.data
        new_password.create_new_password(email,password)
        
        flash("Tu nueva contraseña a sido creada.")
        return redirect(url_for('rg.loggin'))
    return render_template("restore_password_form.html", **context)


@blue_rg.route('/delete/<id>')
@login_required
def delete(id):
    from app.controllers.queries.querys import del_comment
    
    del_comment.del_comment_user(id=id)
    
    # esto es para que más adelante no elimine los comentarios que no creó el usuario
    #usuario = current_user.comments[0]
    #print(usuario.user_id, type(usuario))
    
    
    return redirect(url_for('blue_dashboard.dashboard'))
