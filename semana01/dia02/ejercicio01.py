numeros_arreglo = []
cantidad = int(input("How many numbers are you going to process?"))
recorrido = 0
suma = 0

#for recorrido in range(cantidad):
while (recorrido < cantidad):
    numeros_arreglo.append(float(input("Number [" + str(recorrido + 1) + "] ")))
    suma = suma + numeros_arreglo[recorrido]
    recorrido = recorrido + 1
    
numeros_tupla = tuple(sorted(numeros_arreglo))
print(numeros_tupla)
print("Max: ",max(numeros_tupla))
print("Min: ",min(numeros_tupla))
if (recorrido > 0):
    print("Avg: ", suma / cantidad)


