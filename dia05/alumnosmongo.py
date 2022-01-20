from pymongo import MongoCLient

cliente = MongoClient('mongodb://localhost:27017') #Este puerto se ve en el Laragon

db = cliente['codigog11'] #Verificar su existencia con show databases;

col_alumnos = db['alumnos']; #Verificar su existencia con show collections;

id_alumno = col_alumnos.insert_one({"nombre":"José Carlos Cervantes","email":"jocacermac@gmail.com","nota":7})

print(id_alumno);