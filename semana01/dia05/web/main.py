from flask import Flask
from flask import render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

#CONFIGURANDO CONEXIÓN CON LA BASE DE DATOS DE MYSQL EN CLEVER-CLOUD.
app.config['MYSQL_HOST'] = 'bfjtrylmfbvqi8qxgomu-mysql.services.clever-cloud.com'
app.config['MYSQL_DB'] = 'bfjtrylmfbvqi8qxgomu'
app.config['MYSQL_USER'] = 'upkrgdleu9co4f0d'
app.config['MYSQL_PASSWORD'] = 'Pxmic8eiPE0YVRrPfwKU'

mysql = MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('select id, sistema, procesador, memoria from computadoras')
    recordset = cursor.fetchall()
    cursor.close()
    
    context = {
        'recordset':recordset
    }
    
    return render_template('index.html',**context)

app.run(debug=True,port=4000)