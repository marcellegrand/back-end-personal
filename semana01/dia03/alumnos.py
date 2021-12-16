#PROGRAMA CRUD DE ALUMNOS
import tabulate

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

def buscar(email):
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

def registrar():
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

def listar():
    rotular("LISTAR")

    if (len(alumnos) > 0):
        cabeceras = alumnos[0].keys()
        registros = [x.values() for x in alumnos]  
        print(tabulate.tabulate(registros,cabeceras))
    else:
        print("***¡¡SIN REGISTRO!!***")
    pausar()

def actualizar():
    rotular("ACTUALIZAR")

    email = input("Ingrese EMAIL del alumno a actualizar:")   
    posicion = buscar(email)
    
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

def eliminar():
    rotular("ELIMINAR")
    
    email = input("Ingrese EMAIL del alumno a eliminar:")   
    posicion = buscar(email)
    
    if (posicion >= 0):
        alumno = alumnos[posicion]
        confirmacion = input("¿Seguro que desea ELIMINAR a " + alumno['email'] + " (S/N)?")
        
        if (confirmacion == 'S'):
            alumnos.pop(posicion)
            print("***¡¡ELIMINADO!!***")
    else:
        print("***¡¡NO ENCONTRADO: " + email + "!!***")
    pausar()        
       
#PROGRAMA PRINCIPAL 
opcion = 1
pausa = 0
alumnos = []
while (opcion >= 1 and opcion <= 4):
    print("****************************************")
    print("******SISTEMA ACADEMICO DE ALUMNOS******")
    print("****************************************")
    menu()
    
    opcion = int(input("Ingrese una OPCIÓN: "))
    if (opcion == 1):
        registrar()
    elif (opcion == 2):
        listar()
    elif (opcion == 3):
        actualizar()
    elif (opcion == 4):
        eliminar()
    elif (opcion == 5):
        rotular("¡GRACIAS!")
    else:
        rotular("¡OPCIÓN INVÁLIDA!")
    

