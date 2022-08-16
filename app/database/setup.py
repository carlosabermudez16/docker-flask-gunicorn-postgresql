from sqlalchemy import create_engine
import logging

logging.basicConfig(level=logging.DEBUG)


def create_tables(app,db, config_class):
    
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
                uri =app.config['SQLALCHEMY_DATABASE_URI']              
                name = 'Postgresql_docker'
                
            #engine.execute("CREATE TABLE IF NOT EXISTS usuarios(id serial, nombre varchar(15), telefono varchar(15))")
            
            
            engine = db.create_engine(uri,{})
            logging.debug(f"\nConexión a base de datos {name} exitosa!")

    except:
        
        logging.debug('\nError en la creación de la tabla: ')
        logging.debug(db.create_engine(uri,{}))
        engine = None
    
    return db.create_all(engine)
