from flask_mail import Message
from smtplib import SMTPException
from flask import current_app, render_template, url_for
from app import mail

from .token import generate_confirmation_token

def send_email(user_email,username):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for('rg.confirm_email', token=token, _external=True)
    with current_app.app_context():
        try:
            msg = Message('Registro exitoso!',
                  sender = current_app.config['MAIL_USERNAME'],
                  recipients= [user_email])
            msg.html = render_template('email.html', username = username, confirm_url=confirm_url)
            
            mail.send(msg)
        except SMTPException:
            # logger.exception("Ocurrió un error al enviar el correo")
            print("Ocurrió un error al enviar el correo")

def send_email_restore_pass(user_email,username):
    token = generate_confirmation_token(user_email)
    confirm_url = url_for('rg.confirm_restore_password', token=token, _external=True)
    with current_app.app_context():
        try:
            msg = Message('Crear nueva contraseña',
                  sender = current_app.config['MAIL_USERNAME'],
                  recipients= [user_email])
            msg.html = render_template('restore_password_mail.html', username = username, confirm_url=confirm_url)
            
            mail.send(msg)
        except SMTPException:
            # logger.exception("Ocurrió un error al enviar el correo")
            print("Ocurrió un error al enviar el correo")


    
def date_format(value):
    months = ("Enero","Febrero","Marzo","Abril","Mayo","Junio",
              "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre")
    month = months[value.month - 1]
    
    return f"{value.day} de {month} del {value.year}"