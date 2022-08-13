from wtforms import Form
from wtforms import StringField, HiddenField, TextAreaField
from wtforms import EmailField
from wtforms import PasswordField, BooleanField
from wtforms.validators import DataRequired, Email, Length, ValidationError, EqualTo
from app.database.model import User



def length_honeypot(form, field):
    if len(field.data) > 0:
        raise ValidationError('El campo debe estar vacio.')

class CreateForm(Form):
    # Los atributos usados aquí se transforma en campos de formulario
    username = StringField('Username', validators=
                           [
                            DataRequired(message = 'El username es requerido'),
                            Length(min=4,max=25,message='Ingrese un username valido')
                            ]
                           )
    email = EmailField('Email', validators=
                       [
                        DataRequired(message = 'El username es requerido'),
                        Email(message='Ingrese un email valido')
                        ]
                       )
    password = PasswordField('Password', validators=
                             [DataRequired(message='El password es requerido')]
                             )
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(),
                                     EqualTo('password')])
    honeypot = HiddenField('',[length_honeypot])

    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        
        if user is not None:
            raise ValidationError(f'El usuario {username} ya se encuentra registrado!', 'danger')

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email ya se encuentra registrado!", 'danger')
        

class LoginForm(Form):
    
    username = StringField('Username', validators=
                           [
                            DataRequired(message = 'El username es requerido'),
                            Length(min=4,max=25,message='Ingrese un username valido')
                            ]
                           )
    
    password = PasswordField('Password', validators=
                             
                             [DataRequired(message='El password es requerido')]
                             )
    
    remember = BooleanField('Remember Me')
    

class CommentForm(Form):
    comment =   TextAreaField('comment',validators=
                             [DataRequired(message='Escribe un comentario')])
    

class RestorePassMailForm(Form):
    email = EmailField('Email', validators=[
                        DataRequired(message = 'El username es requerido'),
                        Email(message='Ingrese un email valido')
                        ])

class RestorePassForm(Form):
    password = PasswordField('Ingresa la nueva contraseña', 
                             validators=[
                                DataRequired(message="Ingresa una contraseña."),
                                EqualTo('confirm', message="La contraseña debe ser igual")
                                ])
    confirm = PasswordField('Repite la contraseña', 
                            validators=[
                                DataRequired(message="Ingresa una contraseña.")
                                ])
    


