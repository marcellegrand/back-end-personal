#PROGRAMA CRUD DE ALUMNOS
import tabulate

print("****************************************")
print("******SISTEMA ACADEMICO DE ALUMNOS******")
print("****************************************")
print("[1] REGISTRAR")
print("[2] LISTAR")
print("[3] ACTUALIZAR")
print("[4] ELIMINAR")
print("[5] SALIR")

opcion = 1
pausa = 0
alumnos = []
while (opcion >= 1 and opcion <= 4):
    print("****************************************")
    print("******SISTEMA ACADEMICO DE ALUMNOS******")
    print("****************************************")
    print("[1] REGISTRAR")
    print("[2] LISTAR")
    print("[3] ACTUALIZAR")
    print("[4] ELIMINAR")
    print("[5] SALIR") 
    
    opcion = int(input("Ingrese una OPCIÓN: "))
    if (opcion == 1):
        print("*********************")
        print("******REGISTRAR******")
        print("*********************")
        nombre = input("Ingrese NOMBRE:")
        email = input("Ingrese EMAIL:")
        celular = input("Ingrese CELULAR:")
        objAlumno = {
            'nombre':nombre,
            'email':email,
            'celular':celular
        }
        alumnos.append(objAlumno)
        print("***¡¡REGISTRADO!!***")
        pausa = input("Presione una tecla para continuar")
    elif (opcion == 2):
        print("******************")
        print("******LISTAR******")
        print("******************") 
        
        registros = []
        if (len(alumnos) > 0):
            cabeceras = alumnos[0].keys()
            registros = [alumno.values() for alumno in alumnos]  
            '''
            for alumno in alumnos:
                registros.append(alumno.values())
            '''
                
            print(tabulate.tabulate(registros,cabeceras))
        else:
            print("***¡¡SIN REGISTRO!!***")
        pausa = input("Presione una tecla para continuar")
    elif (opcion == 3):
        print("**********************")
        print("******ACTUALIZAR******")
        print("**********************") 
        email = input("Ingrese EMAIL del alumno a actualizar:")   
        indice = 0
        posicion = -1
        objAlumno = {}
        while (indice < len(alumnos)):
            objAlumno = alumnos[indice]
            for valor in objAlumno.values():
                if (valor == email):
                    posicion = indice
                    break
            if (posicion >= 0):
                break
            indice = indice + 1
        
        if (posicion >= 0):
            nombre = input("Ingrese NUEVO [NOMBRE ANTERIOR -> " + objAlumno['nombre'] + "]:")
            email = input("Ingrese NUEVO [EMAIL ANTERIOR -> " + objAlumno['email'] + "]:")
            celular = input("Ingrese NUEVO [CELULAR ANTERIOR -> " + objAlumno['celular'] + "]:")
            
            objAlumno = {
                'nombre':nombre,
                'email':email,
                'celular':celular
            }
            alumnos[posicion] = objAlumno
            print("***¡¡ACTUALIZADO!!***")
        else:
            print("***¡¡NO ENCONTRADO: " + email + "!!***")
        pausa = input("Presione una tecla para continuar")        
    elif (opcion == 4):
        print("********************")
        print("******ELIMINAR******")
        print("********************")        
        email = input("Ingrese EMAIL del alumno a eliminar:")   
        indice = 0
        posicion = -1
        objAlumno = {}
        while (indice < len(alumnos)):
            objAlumno = alumnos[indice]
            for valor in objAlumno.values():
                if (valor == email):
                    posicion = indice
                    break
            if (posicion >= 0):
                break
            indice = indice + 1
        
        if (posicion >= 0):
            print('NOMBRE: ' + objAlumno['nombre'])
            print('EMAIL: ' + objAlumno['email'])
            print('CELULAR: ' + objAlumno['celular'])
            confirmacion = input("¿Seguro que desea ELIMINAR (S/N)?")
            
            if (confirmacion == 'S'):
                alumnos.pop(posicion)
                print("***ELIMINADO!!***")
        else:
            print("***¡¡NO ENCONTRADO: " + email + "!!***")
        pausa = input("Presione una tecla para continuar")        
    elif (opcion == 5):
        print("*********************")
        print("******¡GRACIAS!******")
        print("*********************")        
    else:
        print("*****************************")
        print("******¡OPCIÓN INVÁLIDA!******")
        print("*****************************")     
    

