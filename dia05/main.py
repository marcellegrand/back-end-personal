from flask import Flask
from flask import jsonify
from flask import request
from flask import Response

from bson import json_util
from bson.objectid import ObjectId

from flask_pymongo import PyMongo

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/codigog11'

mongo = PyMongo(app)

@app.route('/')
def index():
    return jsonify({'mensaje':'api flask mongo'})

@app.route('/add_alumno',methods=['POST'])
def addAlumno():
    nombre = request.json['nombre']
    email = request.json['email']
    nota = request.json['nota']
    
    id = mongo.db.alumnos.insert_one(
        {
            'nombre':nombre,
            'email':email,
            'nota':nota
        }
    )

    response = jsonify(
        {
            '_id':str(id),
            'nombre':nombre,
            'email':email,
            'nota':nota
        }
    )
    response.status_cod = 201
    return response

@app.route('/list_alumnos',methods=['GET'])
def listAlumnos():
    col_alumnos = mongo.db.alumnos.find();
    response = json_util.dumps(col_alumnos)
    return Response(response,mimetype="application/json") 
    
@app.route('/get_alumno/<id>',methods=['GET'])
def getAlumno(id):
    doc_alumno = mongo.db.alumnos.find_one({'_id':ObjectId(id)})
    response = json_util.dumps(doc_alumno)
    return Response(response,mimetype="application/json")

@app.route('/upd_alumno/<id>',methods=['PUT'])
def updAlumno(id):
    nombre = request.json['nombre']
    email = request.json['email']
    nota = request.json['nota']
    
    mongo.db.alumnos.update_one(
        {'_id':ObjectId(id)},
        {'$set':{
            'nombre':nombre,
            'email':email,
            'nota':nota
        }}
    )
    
    response = jsonify({'mensaje':'alumno actualizado'})
    response.status_cod = 201
    return response

@app.route('/del_alumno/<id>',methods=['DELETE'])
def delAlumno(id):
    mongo.db.alumnos.delete_one({'_id':ObjectId(id)})
    response = jsonify({'mensaje':'alumno eliminado'})
    response.status_cod = 200
    return response
    

if __name__ == "__main__":
    app.run(debug=True,port=5000)