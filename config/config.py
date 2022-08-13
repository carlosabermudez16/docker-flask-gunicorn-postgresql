import os
from dotenv import load_dotenv



load_dotenv()



class Config(object):
    # creamos un identificaor para nuestro formulario
    # cuando se valide del request por parte del servidor hay que validar
    # que el id haga match con el que se envío en el request
    SECRET_KEY = os.getenv("SECRET_KEY") # debe ir en el archivo env
    SECURITY_PASSWORD_SALT = os.getenv("SECURITY_PASSWORD_SALT")
    
    
    MAIL_SERVER   = os.getenv('MAIL_SERVER')
    MAIL_PORT     = 465
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_USE_TLS  = False
    MAIL_USE_SSL  = True
    
    DATABASE_CONNECT_OPTIONS = {}
    
    # Hilos de aplicación. Una suposición general común es usar 2 por cada 
    # núcleo de procesador disponible: para manejar las solicitudes entrantes 
    # usando uno y realizar operaciones en segundo plano usando el otro.
    THREADS_PER_PAGE = 2
    
    
    # Habilite la protección contra *Falsificación de solicitud entre sitios (CSRF)*
    CSRF_ENABLED     = True
    # Utilice una clave segura, única y absolutamente secreta para firmar los datos.
    CSRF_SESSION_KEY = "secret"
    


class DevelopmentConfig(Config):
    
    host,database,user,password,puerto,driver = os.getenv("HOST2"),os.getenv("DATABASE2"),os.getenv("USER2"),os.getenv("PASSWORD2"),os.getenv("PORT2"),os.getenv("DRIVER2")
    ruta = f'{driver}://{user}:{password}@{host}:{puerto}/{database}'
    
    SQLALCHEMY_DATABASE_URI = ruta
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class DevDocker(Config):
    
    host,database,user,password,puerto,driver = os.getenv("HOST_DOCKER"),os.getenv("DATABASE_DOCKER"),os.getenv("USER_DOCKER"),os.getenv("PASSWORD_DOCKER"),os.getenv("PORT_DOCKER"),os.getenv("DRIVER_DOCKER")
    ruta = f'{driver}://{user}:{password}@{host}:{puerto}/{database}'
    
    SQLALCHEMY_DATABASE_URI = ruta
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False

class CloudDev(Config):
    host,database,user,password,puerto,driver = os.getenv("HOST_CLOUD"),os.getenv("DATABASE_CLOUD"),os.getenv("USER_CLOUD"),os.getenv("PASSWORD_CLOUD"),os.getenv("PORT_CLOUD"),os.getenv("DRIVER_CLOUD")
    ruta = f'{driver}://{user}:{password}@{host}:{puerto}/{database}'
    
    SQLALCHEMY_DATABASE_URI = ruta
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    
class ProductionConfig(Config):
    
    host,database,user,password,puerto,driver = os.getenv("HOST"),os.getenv("DATABASE"),os.getenv("USER"),os.getenv("PASSWORD"),os.getenv("PORT"),os.getenv("DRIVER")
    ruta = f'{driver}://{user}:{password}@{host}:{puerto}/{database}'
    
    SQLALCHEMY_DATABASE_URI = ruta
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    DEBUG = False    

        
    
    
    
    
    
    
    
    
    