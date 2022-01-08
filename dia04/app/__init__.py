#Importamos el framework Flask
from flask import Flask

#Importamos flask bootstrap para integrarlo con flask
from flask_bootstrap import Bootstrap

#Importamos los Blueprints
from .admin import admin

#Importamos las configuraciones
from .config import Config

#Función para crear la app de flask
def create_app():
    app = Flask(__name__)
    
    #Agregamos bootstrap a la app
    bootstrap = Bootstrap(app)
    
    #Agrega parámetros de configuración a la aplicación
    app.config.from_object(Config)
    
    #Registramos los blueprints
    app.register_blueprint(admin)

    return app

