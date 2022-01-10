#Importamos render_template para renderizar plantillas de jinja2
from flask import render_template

#Permite hacer cuadros de mensaje agradables en la interfaz web
from flask import flash

#Permite redireccionar rutas
from flask import redirect

#Permite hacer rutas a views, projects, etc
from flask import url_for

#Para escribir y leer desde variables de sesión
from flask import session

#Importamos el 'admin' del paquete actual 'admin'
from . import admin

#Importamos los formularios
from app.forms import LoginForm

##########FIREBASE4##########
import pyrebase

config = {
  "apiKey": "AIzaSyBc92EOVXBAszZarkNrWcdBLOKJbAcbU6k",
  "authDomain": "portafolio-811dc.firebaseapp.com",
  "databaseURL": "https://portafolio-811dc-default-rtdb.firebaseio.com",
  "projectId": "portafolio-811dc",
  "storageBucket": "portafolio-811dc.appspot.com",
  "messagingSenderId": "819809137842",
  "appId": "1:819809137842:web:517d325f0db9e8752885ab",
  "measurementId": "G-70HS411F9J"
};

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
##########FIREBASE4##########

############# FIRESTORE ##################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#########################################################


@admin.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    
    #Código para realizar el login de usuarios
    if login_form.validate_on_submit():
        #Obtenemos el usuario y el password del formulario
        usuarioData = login_form.usuario.data
        passwordData = login_form.password.data
        
        try:
            usuario = auth.sign_in_with_email_and_password(usuarioData,passwordData)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.proyectos'))
            #flash(auth.get_account_info(usuario['idToken']))        
        except:
            flash('Invalid user or password!')
            
    return render_template('admin/login.html',**context)

@admin.route('/proyectos')
def proyectos():
    if ('token' in session):
        colProyectos = db.collection('proyectos')
        proyecto_form = ProyectoForm()
        
        if proyecto_form.validate_on_submit():
            #CAPTURAMOS VALORES DE USUARIO Y PASSWORD
            nombreData = proyecto_form.nombre.data
            descripcionData = proyecto_form.descripcion.data
            urlData = proyecto_form.url.data
            
            #CREAR DICCIONARIO
            data = {
                'nombre': nombreData,
                'descripcion':descripcionData,
                'url':urlData
            }
            
            colProyectos.document().set(data)
        
        
        docProyectos = colProyectos.get()        
        lstProyectos = []
        for doc in docProyectos:
            dicProyecto = doc.to_dict()
            lstProyectos.append(dicProyecto)
    
        print(lstProyectos)
        

        context = {
            'proyectos':lstProyectos,
            'proyecto_form':proyecto_form
        }
        
        return render_template('admin/proyectos.html',**context)
    else:
        return redirect(url_for('admin.login'))
        
@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.login'))