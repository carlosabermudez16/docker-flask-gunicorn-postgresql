
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from flask_login import UserMixin
import logging

logging.basicConfig(level=logging.DEBUG)

class User(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True)
    email = db.Column(db.String(40), unique = True)
    password = db.Column(db.Text)
    public_id = db.Column(db.String(50))
    rol = db.Column(db.String(15))
    comments = db.relationship('Comment', cascade="delete,merge")
    created_date = db.Column(db.DateTime, default = datetime.now)
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmed_on = db.Column(db.DateTime, nullable=True)
    
    def __init__(self, username, password, email, public_id):
        self.username = username
        self.password = self.__create_password(password=password)
        self.email = email
        self.public_id = public_id
    
    
    def __create_password(self,password):
        return generate_password_hash(password=password,method='sha256')
    
    def verify_password(self,password):
        return check_password_hash(self.password,password)

    def __repr__(self) -> str:
        return '<usuarios {}>'.format(self.username)
    
    logging.debug('tabla 1 creada')

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuarios.id', ondelete="CASCADE"))
    text = db.Column(db.Text)
    created_date = db.Column(db.DateTime, default = datetime.now)

    logging.debug('tabla 2 creada')

