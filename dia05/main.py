from flask import Flask
#Permite retornar datos en formato json. Con esto se hacen las APIs
from flask import jsonify
#Para permitir solicitudes de petición
from flask import request
#Para poder crear objetos ORM
from flask_marshmallow import Marshmallow
#Para poder integrar SQLAlchemy con Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Configurando el acceso a la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://upkrgdleu9co4f0d:Pxmic8eiPE0YVRrPfwKU@bfjtrylmfbvqi8qxgomu-mysql.services.clever-cloud.com:3306/bfjtrylmfbvqi8qxgomu'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)

#Creamos tablas en la base de datos
#Es importantísimo que las clases acá creadas hereden del db.model (modelo de la base de datos)
#Así, más adelante, cuando se invoque el db.create_all(), definirá todas las clases, u objetos
#de la base de datos, conforme a la definición que se haya dado
class Alumno(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(100),unique=True)
    
    def __init__(self,name,email):
        self.name = name
        self.email = email

#Con esto se crean las tablas en la base de datos
db.create_all()

#Creamos los esquemas
class AlumnosSchema(ma.Schema):
    class Meta:
        fields = ('id','name','email')
        
@app.route('/')
def index():
    return jsonify(
        {
            'status':'OK',
            'message':'Welcome to APIREST with Flask'
        }
    )

alumno_schema = AlumnosSchema()
@app.route('/agregar_alumno',methods=['POST'])
def agregar_alumno():
    #Capturamos los valores
    name = request.json['name']
    email = request.json['email']
    
    #Insertamos el registro en la base de datos
    nuevoAlumno = Alumno(name,email)
    db.session.add(nuevoAlumno)
    db.session.commit()
    
    return alumno_schema.jsonify(nuevoAlumno)

alumnos_schema = AlumnosSchema(many=True) 
@app.route('/listar_alumnos')
def listar_alumnos():
    lstAlumnos = Alumno.query.all()
    #print(lstAlumnos)
    dataAlumnos = alumnos_schema.dump(lstAlumnos)
    return jsonify(dataAlumnos)

@app.route('/actualizar_alumno/<id>',methods=['PUT'])
def actualizar_alumno(id):
    alumno = Alumno.query.get(id)

    #Capturamos los nuevos valores
    name = request.json['name']
    email = request.json['email']
    
    #Actualizamos con los nuevos valores
    alumno.name = name
    alumno.email = email
    
    db.session.commit()
    
    return alumno_schema.jsonify(alumno)

@app.route('/eliminar_alumno/<id>',methods=['DELETE'])
def eliminar_alumno(id):
    alumno = Alumno.query.get(id)
    db.session.delete(alumno)
    db.session.commit()
    
    return alumno_schema.jsonify(alumno)

@app.route('/mostrar_alumno/<id>')
def mostrar_alumno(id):
    alumno = Alumno.query.get(id)
    return alumno_schema.jsonify(alumno)
    
if (__name__ == '__main__'):
    app.run(debug=True,port=5000)