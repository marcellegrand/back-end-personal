from flask import Flask
from flask import render_template

'''Librerías para usar Firebase'''
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

'''Credenciales de acceso a Firebase, para acceder al servicio de Firestore Database'''
cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

parameters = {
    'nombre':'Marcel Johan',
    'apellido':'Lazo de la Vega Velarde',
    'foto':'https://firebasestorage.googleapis.com/v0/b/portafolio-811dc.appspot.com/o/proyectos%2Fmoi.jpg?alt=media&token=69987ffc-a200-410e-b5bb-7826b67d5773',
    'biografia':'Computer Science, IT Support',
    'pais':'Perú',
    'ciudad':'Arequipa',
    'distrito':'JLByR',
    'direccion':'Villa Médica, Torre 1, Dpto 903'
}

@app.route('/')
def home():
    return render_template('home.html',**parameters)

@app.route('/portafolio')
def portafolio():
    '''Obtenemos la colección deseada desde Firebase Database'''
    colProyectos = db.collection('proyectos')
    '''Obtenemos los documentos desde la colección'''
    docProyectos = colProyectos.get()
    '''Inicializamos un arreglo vacío donde se cargarán los documentos, pero como diccionarios'''
    lstProyectos = []
    '''Inicializamos una variable de iteración'''
    intRecorrido = 1
    
    for docProyecto in docProyectos:
        #print(docProyecto.to_dict())
        dicProyecto = docProyecto.to_dict()
        indice = {'indice':intRecorrido}
        dicProyecto.update(indice)
        lstProyectos.append(dicProyecto)
        intRecorrido += 1
 
    context = {
        'proyectos':lstProyectos     
    }
    
    '''Agregamos ahora las claves y valores del diccionario parameters'''
    for clave,valor in parameters.items():
        tupla = {clave:valor}
        context.update(tupla)
    
    return render_template('portafolio.html',**context)

@app.route('/about')
def about():
    return render_template('about.html',**parameters)

@app.route('/contact')
def contact():
    return render_template('contact.html',**parameters)

if __name__ == '__main__':
    app.run(debug=True,port=5000)