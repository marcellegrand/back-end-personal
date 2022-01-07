from flask import Flask
from flask import render_template
from flask import request


import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

app = Flask(__name__)

context = {
    'nombre':'Marcel Lazo de la Vega Velarde',
    'imagen':'https://firebasestorage.googleapis.com/v0/b/portafolio-811dc.appspot.com/o/proyectos%2Fportafolio1.png?alt=media&token=e1de43a6-5996-40b9-9628-036bea1bfdd1',
    'biografia':'Computer Science'
}

@app.route('/')
def home():
    return render_template('home.html',**context)

@app.route('/portafolio')
def portafolio():
    colProyectos = db.collection('proyectos')
    docProyectos = colProyectos.get()
    lstProyectos = []
    
    for docProyecto in docProyectos:
        #print(docProyecto.to_dict())
        dicProyecto = docProyecto.to_dict()
        lstProyectos.append(dicProyecto)
        
    context = {
        'proyectos':lstProyectos,
        'nombre':'Marcel Lazo de la Vega Velarde',
        'imagen':'https://firebasestorage.googleapis.com/v0/b/portafolio-811dc.appspot.com/o/proyectos%2Fportafolio1.png?alt=media&token=e1de43a6-5996-40b9-9628-036bea1bfdd1',
        'biografia':'Computer Science'        
    }
    
    return render_template('portafolio.html',**context)

@app.route('/about')
def about():
    return render_template('about.html',**context)

@app.route('/contact')
def contact():
    return render_template('contact.html',**context)

if __name__ == '__main__':
    app.run(debug=True,port=5000)