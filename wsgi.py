from app import create_app
import os
#settings_module = os.getenv('APP_PROD')
#settings_module = os.getenv('APP_DEV')
settings_module = os.getenv('APP_DOCKER')
#settings_module = os.getenv('APP_CLOUD')

app = create_app(config_class = settings_module)
    
    

