from app.database.model import User, db, Comment
from werkzeug.security import generate_password_hash

class QuerysAll:
    def __init__(self,model_user=None, model_db=None, model_comment=None):
        self.model_user = model_user
        self.model_db = model_db
        self.model_comment = model_comment

    @classmethod # colocando este decorador ya no es necesario crear una isntancia para
                 # acceder al método post_register, sino que puedes entrar directamente
                 # usando --> QuerysAll.post_register(...) 
    def post_register(self, username,password,email, public_id):
        # creamos la instancia del modelo
        user = User(username = username,
                    password = password,
                    email = email,
                    public_id = public_id)
        # realizamos la persitencia en la base de datos
        db.session.add(user) # adicionamos el registro
        db.session.commit() # confirmamos el registro
        
        return user
    
    def post_loggin(self,username):
        user = User.query.filter_by(username = username).first()
        return user
    
    def post_comment(self, user_id,text):
        comment = Comment( user_id = user_id, 
                            text = text,
                            )
        db.session.add(comment)
        db.session.commit()
    
    def get_comment(self):
        
        return Comment.query.join(User).add_columns(User.username,
                                                    Comment.id,
                                                    Comment.text,
                                                    Comment.created_date
                                                    )

    def confirmed(self, user):
        from datetime import datetime
        user.confirmed = True
        user.confirmed_on = datetime.now()
        db.session.add(user)
        db.session.commit()
    
    def get_email(self,email):
        user = User.query.filter_by(email=email).first_or_404()
        return user
    
    def create_new_password(self, email, password):
        user = User.query.filter_by(email=email).first()
        user.password = generate_password_hash(password=password,method='sha256')
        db.session.commit()
    
    def save_token(self, username, token):
        user = User.query.filter_by(username=username).first()
        user.tokens_jwt = token
        db.session.commit()
    
    def get_token(self, username):
        user = User.query.filter_by(username=username).first_or_404()
        token = user.tokens_jwt
        return token

    def get_public_id(self, data):
        token = User.query.filter_by(public_id=data).first()
        usuario = token.username
        return usuario

    def del_comment_user(self, id):
        query = Comment.query.filter_by(id=id).first()
        db.session.delete(query)
        db.session.commit()
    
    
    
comments = QuerysAll(model_user= User, model_comment= Comment)

save_register = QuerysAll(model_user= User, model_db= db)

save_loggin = QuerysAll(model_user= User)

save_comment = QuerysAll(model_db= db, model_comment= Comment)

confirmed_register = QuerysAll(model_user = User, model_db=db)

query_email = QuerysAll(model_user=User,model_db= db)

new_password = QuerysAll(model_user=User, model_db=db)

add_token = QuerysAll(model_user=User, model_db=db)

get_token = QuerysAll(model_user= User)

del_comment = QuerysAll(model_db=db, model_comment=Comment)

get_public_id = QuerysAll(model_user=User)
