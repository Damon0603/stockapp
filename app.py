
import os 
from sys import exit
from stock_dashboard.home import blueprint
from flask import Flask,Blueprint

class ProdConfig:
    ENV = 'production'
    DEBUG = False

class DebugConfig:
    ENV = 'development'
    DEBUG = True

class TestConfig:
    ENV = 'test'
    DEBUG = True
    TESTING = True
    WTF_CSRF_ENABLED = False


# Creating a dictionary that maps the config name to the actual config object

config_dict = {
    'Prod': ProdConfig,
    'Dev': DebugConfig,
    'Test': TestConfig
}




def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(blueprint)
    return app



DEBUG = (os.environ.get('DEBUG', 'False') == 'True')

get_config_mode = 'DEBUG' if DEBUG else 'PROD'

try:
    config = config_dict[get_config_mode.capitalize()]
except KeyError:
    exit('Error: Invalid <config_mode>. Expected values [Debug, Prod]')


app = create_app(config)

if DEBUG:
    app.logger.info('Running in debug mode')
else:
    app.logger.info('Running in production mode')

if __name__ == '__main__':
    app.run()




