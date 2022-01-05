#Ejemplo de decorador
def mayusculas(func):
    def envoltura(texto):
        return func(texto).upper()
    return envoltura

#@mayusculas
def mensaje(nombre):
    return 'hola ' + nombre

print(mensaje('marcel'))