'''
Importamos la clase 'Flask' desde la librería 'flask'
'''
from flask import Flask

'''
Creamos un objeto llamado 'app' instanciado desde la clase 'Flask'
'''
app = Flask(__name__)

'''
Primer ejemplo de @decorator. Sirven para redefinir métodos o funciones de los objetos
'''
@app.route('/')
def index():
    return '<H1>Hello, Web World!</h1>'

'''
Ejecutamos la aplicación, invocando el método run() del objeto 'app'
'''
app.run()