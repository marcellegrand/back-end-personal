'''Tupla'''
primos = (2,3,5,7,11,13) 
'''Arreglo o lista'''
pares = [2,4,6,8,10,12,14,16,18,20,22] 

'''
Clonamos la tupla y la lista anteriores,
inviertiendo las estructuras resultado
'''
primos2 = list(primos)
pares2 = tuple(pares)

'''Solo los arreglos pueden modificarse'''
primos2.append(17) 
pares.pop()

'''¡¡Las tuplas no son alterables!!'''
#primos.pop()
#pares2.append(14)

'''La función 'sorted' retorna un arreglo o lista'''
primosordenados = sorted(primos,reverse=False)
paresordenados = sorted(pares,reverse=True)

primosordenados.append(17)
primosordenados.append(19)
paresordenados.pop()
paresordenados.pop()

print(primosordenados)
print(paresordenados)