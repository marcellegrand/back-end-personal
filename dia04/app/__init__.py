#Importamos el framework Flask
from flask import Flask

#Importamos flask bootstrap para integrarlo con flask
from flask_bootstrap import Bootstrap

#Importamos los Blueprints
from .admin import admin

#Función para crear la app de flask
def create_app():
    app = Flask(__name__)
    
    #Agregamos bootstrap a la app
    bootstrap = Bootstrap(app)
    
    #Registramos los blueprints
    app.register_blueprint(admin)

    return app

