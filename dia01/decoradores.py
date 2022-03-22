'''
Ejemplo de decorador:
Los decoradores siempre recibirán como parámetro una función e
interiormente tendrán otra función la cual recibirá el parámetro
o parámetros de la función original. Esa función interna es la que
hace el maquillaje del comportamiento de la función original.
'''
def mayusculas(p_function):
    def envoltura(p_phrase,p_name):
        return p_function(p_phrase,p_name).upper()
    return envoltura

'''
Ejemplo de aplicación de un decorador:
El decorador es una función que ahora maquillará el comportamiento
o funcionalidad de la función sobre la cual sea puesto
'''
@mayusculas
def saludo_con_decorador(frase,nombre):
    return frase + ', ' + nombre

def saludo_sin_decorador(frase,nombre):
    return frase + ', ' + nombre

print(saludo_con_decorador('hola','marcel'))
print(saludo_sin_decorador('hola','marcel'))