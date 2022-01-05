from flask import Flask
from flask import render_template
from flask import request
import requests

URL = 'https://api.github.com/users/marcellegrand'
data = requests.get(URL)
context = data.json()

print(context)

app = Flask(__name__)

lstAutos = ['Audi','BMW','Lexus','Jaguar']

@app.route('/index')
#def index():
#   return 'HOLA MUNDO FLASK'

#def index():
#   nombre = request.args.get('nombre','no hay nombre')
#   return render_template('index.html',nombre=nombre)

def index():
    nombre = request.args.get('nombre','no name')
    context = {
        'nombre':nombre,
        'autos':lstAutos
    }
    return render_template('index.html',**context)

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