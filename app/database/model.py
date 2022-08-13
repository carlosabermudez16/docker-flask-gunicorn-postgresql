from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import db
from sqlalchemy import Column, String, Integer, Text
from sqlalchemy import DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'usuarios'
    
    id = Column(Integer, primary_key = True)
    username = Column(String(50), unique = True)
    email = Column(String(40), unique = True)
    password = Column(Text)
    public_id = Column(String(50))
    rol = Column(String(15))
    comments = relationship('Comment', cascade="delete,merge")
    created_date = Column(DateTime, default = datetime.now)
    confirmed = Column(Boolean, nullable=False, default=False)
    confirmed_on = Column(DateTime, nullable=True)
    
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

class Comment(db.Model):
    __tablename__ = 'comments'

    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('usuarios.id', ondelete="CASCADE"))
    text = Column(Text())
    created_date = Column(DateTime, default = datetime.now)


