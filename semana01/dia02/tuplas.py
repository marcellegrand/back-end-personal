primos = (2,3,5,7,11,13) #Tupla
pares = [2,4,6,8,10] #Arreglo

primos2 = list(primos)
pares2 = tuple(pares)

#Solo los arreglos pueden modificarse
primos2.append(17) 
pares.append(12)

primosordenados = sorted(primos,reverse=True)
paresordenados = sorted(pares,reverse=True)

print(primosordenados)
print(paresordenados)