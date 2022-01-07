#Importamos algunas librerías desde Flask
from flask import render_template

#Importamos la funcion create_app de la carpeta app
from app import create_app

app = create_app()

#Creamos las rutas
@app.route('/')
def index():
    return render_template('index.html')