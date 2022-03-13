
'''
Los diccionarios en Python nos permiten almacenar una serie de mapeos (items)
entre dos conjuntos de elementos, llamados keys and values (claves y valores). 
Todos los elementos en el diccionario se encuentran encerrados entre {}
'''
capitales = {
    "Brasil": "Brasilia",
    "Uruguay": "Montevideo",
    "Ecuador": "Quito",
    "Chile": "Santiago"
}
print(capitales)

'''AGREGANDO una nueva clave:valor (item) al diccionario'''
capital = {"Perú": "Lima"}
capitales.update(capital)
capital = {"Colombia": "Bogotá"}
capitales.update(capital)
print(capitales)

'''OBTENIENDO el valor dada una clave; ELIMINANDO la clave:valor del diccionario'''
capital = capitales.pop("Bolivia","No existe")
print(capital)
capital = capitales.pop("Chile","No existe")
print(capital)
print(capitales)

'''IMPRIMIENDO claves y valores'''
print(capitales.keys())
print(capitales.values())

'''RECORRIENDO los items del diccionario.'''
for capital in capitales:
    print(capital,"::",capitales[capital])

'''RECORRIENDO las claves del diccionario.'''
for clave in capitales.keys():
    print(clave,"=>",capitales[clave])

'''RECORRIENDO los valores del diccionario.'''
for valor in capitales.values():
    print(valor)

'''RECORRIENDO las claves y valores del diccionario.'''  
for clave,valor in capitales.items():
    print(clave,"--",valor)



