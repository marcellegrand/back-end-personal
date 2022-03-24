from flask import Flask
from flask import render_template
from flask import request
import requests

app = Flask(__name__)

'''
Vamos importando este diccionario de datos desde la URL de github.
Con esos datos reales alimentaremos los 'templates' de html.
La variable 'context' es un diccionario 
'''
URL = 'https://api.github.com/users/marcellegrand'
data = requests.get(URL)
print(data)
context = data.json()
print(context)

'''
Creamos esta ruta llamada '/index' para probar el envío de parámetros de contexto a la renderización
de una página 'html'. Este variable de tipo json normalmente suele llamarse 'context', pero en nuestro 
ejemplo estamos usando la variable 'parameters'. Obviamente, esta variable es un diccionario.
'''
@app.route('/index')
#def index():
#   return 'HOLA MUNDO FLASK'

#def index():
#   nombre = request.args.get('nombre','no hay nombre')
#   return render_template('index.html',nombre=nombre)
def index():
    #http://127.0.0.1:5000/index?nombre=Marcel&sexo=M
    nombre = request.args.get('nombre','no name')
    sexo = request.args.get('sexo','F')
    if sexo == 'F':
        saludo = 'A'
    else:
        saludo = 'O'
    lstAutos = ['Audi','BMW','Lexus','Jaguar']
    lstConsolas = ('Nintendo Switch','Microsoft XBox One S','Sony PlayStation 4')
    parameters = {
        'nombre':nombre,
        'saludo':saludo,
        'autos':lstAutos,
        'consolas':lstConsolas
    }
    return render_template('index.html',**parameters)

@app.route('/')
def home():
    return render_template('home.html',**context)

@app.route('/portafolio')
def portafolio():
    return render_template('portafolio.html',**context)

@app.route('/about')
def about():
    return render_template('about.html',**context)

@app.route('/contact')
def contact():
    return render_template('contact.html',**context)

if __name__ == '__main__':
    app.run(debug=True,port=5001)