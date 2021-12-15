dias = ["lunes","martes","miércoles","jueves","viernes","sábado","domingo"]
primos = [2,3,5,7,11,13]
fecha = ["martes",14,"diciembre",2021]

print(dias[3:6]) #Desde la posición 3 hasta antes de la posición 6
print(len(dias)) #Imprime la cantidad de elementos en la colección

print(primos) 
primos.append(17)
print(primos)
primos.pop()

for dia in dias:
    print("Día: " + dia)
    
for dia in range(len(dias)):
    print(dias[dia])