import os
from alumnos_libreria import *

'''       
******************
PROGRAMA PRINCIPAL
****************** 
'''
opcion = 1
pausa = 0
archivo = 'alumnos.csv'
separador = ';'
alumnos = []

leerArchivo(alumnos,archivo,separador)
while (opcion >= 1 and opcion <= 4):
    print("****************************************")
    print("******SISTEMA ACADEMICO DE ALUMNOS******")
    print("****************************************")
    menu()
    
    opcion = int(input("Ingrese una OPCIÓN: "))
    if (opcion == 1):
        registrar(alumnos)
    elif (opcion == 2):
        listar(alumnos)
    elif (opcion == 3):
        actualizar(alumnos)
    elif (opcion == 4):
        eliminar(alumnos)
    elif (opcion == 5):
        guardarArchivo(alumnos,archivo)
        rotular("¡GRACIAS!")
    else:
        rotular("¡OPCIÓN INVÁLIDA!")
    

