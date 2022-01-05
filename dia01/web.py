#Primera aplicación web con Python y Flask
from flask import Flask, request

app = Flask(__name__)

#Ruta predeterminada
@app.route('/')
def index():
    return '<h1>BIENVENIDO A MI PAGINA WEB CON FLASK</h1>'

#Ruta específica de ejemplo
@app.route('/greeting')
#http://127.0.0.1:5000/greeting?nombre=Marcel
def greeting():
    nombre = request.args.get('nombre','not defined!')
    return '<h1>Hola {}</h1>'.format(nombre)

@app.route('/sum')
#http://127.0.0.1:5000/sum?n1=10&n2=20
def sum():
    n1 = request.args.get('n1','0')
    n2 = request.args.get('n2','0')
    r = int(n1) + int(n2)
    return '<h1>La suma de {} + {} es {}'.format(n1,n2,r)

@app.route('/substract/<int:n1>/<int:n2>')
#http://127.0.0.1:5000/substract/5/4
def substract(n1=0,n2=0):
    r = n1 - n2
    return '<h1>La resta de {} - {} es {}'.format(n1,n2,r)

@app.route('/calculator',methods=['GET','POST'])
def calculator():
    form = "<form action = 'calculator' method = 'POST'>"
    form += "<input type = 'text' name = 'n1' size = '2'/> + <input type = 'text' name = 'n2' size = '2'/>"
    form += "<input type = 'submit' value='=' />"
    form += "</form>"
    
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        r = int(n1) + int(n2)
        form += '<h2>La suma es {}</h2>'.format(r)
    
    return form
 
#Tarea: 20210104
@app.route('/aritmetic',methods=['GET','POST'])
def aritmetic():
    op = 0
    te = ""
    
    def operator(val):
        op = val  
    
    form = "<form action = 'aritmetic' method = 'POST'>"
    form += "<input type = 'text' name = 'n1' size = '2'/>"
    form += "<button id = 'op_s' action = 'operator(1)'>+</button>"
    form += "<button id = 'op_r' action = 'operator(2)'>-</button>"
    form += "<button id = 'op_m' action = 'operator(3)'>*</button>"
    form += "<button id = 'op_d' action = 'operator(4)'>/</button>"
    form += "<input type = 'text' name = 'n2' size = '2'/>"
    form += "<input type = 'submit' value='=' />"
    form += "</form>"
    
    if request.method == 'POST':
        n1 = request.form['n1']
        n2 = request.form['n2']
        if op == 1: 
            re = int(n1) + int(n2)
            te = "suma"
        if op == 2: 
            re = int(n1) - int(n2)
            te = "resta"
        if op == 3: 
            re = int(n1) * int(n2)
            te = "multiplicación"
        if op == 4: 
            re = int(n1) / int(n2)
            te = "división"
            
        form += '<h2>La ' + te + ' es {}</h2>'.format(re)
    
    return form    

app.run(debug = True)