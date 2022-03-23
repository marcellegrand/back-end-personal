#Primera aplicación web con Python y Flask
from flask import Flask
from flask import request

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
    '''
    El action definido dentro de este form apunta a la ruta definida en este @app.route
    '''
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
    operator = 0
    number_1 = 0
    number_2 = 0
    default_sum = ""
    default_sub = ""
    default_mul = ""
    default_div= ""

    if request.method == 'POST':
        number_1 = int(request.form['number_1'])
        number_2 = int(request.form['number_2'])
        operator = int(request.form['operator'])

    if operator > 0:  
        if operator == 1: 
            result = number_1 + number_2
            text = "suma"
            default_sum = "checked"
        if operator == 2: 
            result = number_1 - number_2
            text = "resta"
            default_sub = "checked"
        if operator == 3: 
            result = number_1 * number_2
            text = "multiplicación"
            default_mul = "checked"
        if operator == 4: 
            if number_2 != 0:
                result = number_1 / number_2
                text = "división"
            else:
                result = 0
                text = "#¡error!"
            default_div = "checked"
            
    form = "<form action = 'aritmetic' method = 'POST'>"
    form += "<input type = 'text' name = 'number_1' size = '2' value = '" + str(number_1) + "'/>"
    form += "<input type = 'radio' name = 'operator' value = '1' " + default_sum + "/> sumar "
    form += "<input type = 'radio' name = 'operator' value = '2' " + default_sub + "/> restar "
    form += "<input type = 'radio' name = 'operator' value = '3' " + default_mul + "/> multiplicar "
    form += "<input type = 'radio' name = 'operator' value = '4' " + default_div + "/> dividir "
    form += "<input type = 'text' name = 'number_2' size = '2' value = '" + str(number_2) + "'/>"
    form += "<input type = 'submit' value='=' />"
    form += "</form>"
    
    if operator > 0:
        if text == "#¡error!":
            form += '<h2>' + text + '</h2>'
        else:    
            form += '<h2>La ' + text + ' es {}</h2>'.format(result)        
        
    return form    

app.run(debug = True)