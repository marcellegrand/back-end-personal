import tabulate
import os

def menu():
    print("[1] REGISTRAR")
    print("[2] LISTAR")
    print("[3] ACTUALIZAR")
    print("[4] ELIMINAR")
    print("[5] SALIR")

def pausar():
    pausa = input("Presione una tecla para continuar")
    
def rotular(rotulo):
    frase = "*****" + rotulo + "*****"
    encierro = "*"
    for recorrido in range(len(frase)):
        encierro = encierro + "*"

    print(encierro)
    print(frase)
    print(encierro)

def buscar(alumnos,email):
    indice = 0
    posicion = -1
    while (indice < len(alumnos)):
        for valor in alumnos[indice].values():
            if (valor == email):
                posicion = indice
                break
        if (posicion >= 0):
            break
        indice = indice + 1
    return posicion

def registrar(alumnos):
    rotular("REGISTRAR")
    nombre = input("Ingrese NOMBRE:")
    email = input("Ingrese EMAIL:")
    celular = input("Ingrese CELULAR:")
    alumno = {
        'nombre':nombre,
        'email':email,
        'celular':celular
    }
    alumnos.append(alumno)
    print("***¡¡REGISTRADO!!***")
    pausar()

def listar(alumnos):
    rotular("LISTAR")

    if (len(alumnos) > 0):
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]  
        print(tabulate.tabulate(registros,cabeceras))
    else:
        print("***¡¡SIN REGISTRO!!***")
    pausar()

def actualizar(alumnos):
    rotular("ACTUALIZAR")

    email = input("Ingrese EMAIL del alumno a actualizar:")   
    posicion = buscar(alumnos,email)
    
    if (posicion >= 0):
        alumno = alumnos[posicion]
        nombre = input("Ingrese NUEVO [NOMBRE ANTERIOR -> " + alumno['nombre'] + "]:")
        email = input("Ingrese NUEVO [EMAIL ANTERIOR -> " + alumno['email'] + "]:")
        celular = input("Ingrese NUEVO [CELULAR ANTERIOR -> " + alumno['celular'] + "]:")
        
        alumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos[posicion] = alumno
        print("***¡¡ACTUALIZADO!!***")
    else:
        print("***¡¡NO ENCONTRADO: " + email + "!!***")
    pausar()

def eliminar(alumnos):
    rotular("ELIMINAR")
    
    email = input("Ingrese EMAIL del alumno a eliminar:")   
    posicion = buscar(alumnos,email)
    
    if (posicion >= 0):
        alumno = alumnos[posicion]
        print('NOMBRE: ' + alumno['nombre'])
        print('EMAIL: ' + alumno['email'])
        print('CELULAR: ' + alumno['celular'])
        confirmacion = input("¿Seguro que desea ELIMINAR (S/N)?")
        
        if (confirmacion == 'S'):
            alumnos.pop(posicion)
            print("***¡¡ELIMINADO!!***")
    else:
        print("***¡¡NO ENCONTRADO: " + email + "!!***")
    pausar()        

def leerArchivo(alumnos,archivo,separador):
    if (os.path.isfile(archivo)):
        objArchivo = open(archivo,'r')
        strContenido = objArchivo.read()
        arrRenglones = strContenido.splitlines()
        for renglon in arrRenglones:
            valores = renglon.split(separador)
            dicRegistro = {
                'nombre':valores[0],
                'email':valores[1],
                'celular':valores[2]
            }
            alumnos.append(dicRegistro)
        objArchivo.close()
    
def guardarArchivo(alumnos,archivo):
    strContenido = ""
    linea = 1
    for alumno in alumnos:
        item = 1
        items = len(alumno.keys())
        if linea > 1:
            strContenido += '\n'
        for valor in alumno.values():
            strContenido += valor
            if item < items:
                strContenido += ';'
            item += 1
        linea += 1
    
    objArchivo = open(archivo,'w')
    objArchivo.write(strContenido)
    objArchivo.close()   