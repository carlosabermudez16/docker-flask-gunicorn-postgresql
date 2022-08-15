from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.DEBUG)


def create_tables(app, db, config_class):
    
    try:
        with app.app_context():  # me permite sicronizar la base de datos con la aplicación
            if config_class == 'prod':
                engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
                
                name = 'Mysql'
                print(name)
            elif config_class == 'dev':
                engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
                
                name = 'Postgresql'
                print(name)
            elif config_class == 'cloud':
                engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
                
                name = 'Postgresql_cloud'
                print(name)
            elif config_class == 'dev_docker':
                engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
                logging.debug(f"\nConexión a base de datos {name} exitosa!")
                name = 'Postgresql_docker'
                logging.debug(name)
                
            
            #db.metadata.create_all(engine)    # crea la tabla en la base de datos que se encuentra en la cadena de conexion(url)                
        
            
        return engine
    except:
        print(f"Error at create_tables()" )
        engine = None
        logging.debug('Error en la creación de la tabla')
        return engine
    