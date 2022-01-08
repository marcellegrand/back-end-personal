#Importamos la clase BLueprint que nos permitirá registrar nuestro módulo al proyecto principal
from flask import Blueprint

admin = Blueprint('admin',__name__,url_prefix='/admin')

#Importamos 'views' del mismo paquete actual: 'admin'
from . import views

