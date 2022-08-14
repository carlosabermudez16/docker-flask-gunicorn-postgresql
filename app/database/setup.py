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
                name = 'Postgresql_docker'
                print(name)
                
            print(f"\nConexión a base de datos {name} exitosa!")
            db.metadata.create_all(engine)    # crea la tabla en la base de datos que se encuentra en la cadena de conexion(url)                
            logging.debug(f'\n\nel valor de entrada es:{config_class}')
            logging.debug("Tabla creada exitosamente!\n")
            logging.debug(app.config['SQLALCHEMY_DATABASE_URI'])
            logging.debug('Creación de tablas exisotamente')
        return True
    except:
        print(f"Error at create_tables()" )
        logging.debug(f'el valor de entrada es:{config_class}')
        logging.debug('Error en la creación de la tabla')
    