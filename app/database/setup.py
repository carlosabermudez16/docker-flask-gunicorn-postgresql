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
                engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])                
                name = 'Postgresql_docker'
                logging.debug(f"\nConexión a base de datos {name} exitosa!")

            db.metadata.create_all(engine)    # crea la tabla en la base de datos que se encuentra en la cadena de conexion(url)                
            logging.debug(db.metadata.create_all(engine))
            logging.debug('Tablas creada exitosamente!')

    except:
        
        logging.debug('\nError en la creación de la tabla: ')
        logging.debug(db.metadata.create_all(engine))

    