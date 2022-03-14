'''
FUNCIONES Y PROCEDIMIENTOS SE DECLARAN DE LA MISMA FORMA
LA FUNCIÓN TIENE LA CLÁUSLA RETURN
EL PROCEDIMIENTO NO TIENE VALOR DE RETORNO
'''
def suma(n1,n2):
    resultado = n1 + n2
    return resultado

a = float(input("First NUMBER: "))
b = float(input("Second NUMBER: "))
r = suma(a,b)
print("Result: ", r)