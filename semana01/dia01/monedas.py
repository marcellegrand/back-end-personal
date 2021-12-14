#ZONA DE IMPORTACIÓN
import locale
locale.setlocale(locale.LC_ALL,'es_PE.UTF-8')

#CONVERSOR DE MONEDAS

#DEFINICIÓN DE VARIABLES
tipocambio_penusd = 4.067
tipocambio_peneur = 4.570

monedaorigen = 0
monedadestino = 0
simboloorigen = "PEN"
simbolodestino = "PEN"
montoinicial = 0
montofinal = 0

print("Monedas:")
print("(1) PEN")
print("(2) USD")
print("(3) EUR")

#montoinicial_number = float(input("Monto inicial: "))
#montoinicial_string = "$ {:,.2f}".format(montoinicial_number)
#montofinal_number = montoinicial_number * tipocambio 
#montofinal_string = "S/ {:,.2f}".format(montofinal_number)

while (monedaorigen < 1 or monedaorigen > 3 or monedadestino < 1 or monedadestino > 3):
    monedaorigen = int(input("Moneda ORIGEN: "))
    monedadestino = int(input("Moneda DESTINO: "))
    montoinicial = float(input("Monto ORIGEN: "))
   
    if (monedaorigen == 1): #PEN
        simboloorigen = "PEN"
        if (monedadestino == 1): #PEN
            simbolodestino = "PEN"
            montofinal = montoinicial
        elif (monedadestino == 2): #USD
            simbolodestino = "USD"
            montofinal = montoinicial / tipocambio_penusd   
        else: #EUR
            simbolodestino = "EUR"
            montofinal = montoinicial / tipocambio_peneur  
    elif (monedaorigen == 2): #USD
        simboloorigen = "USD"
        if (monedadestino == 1): #PEN
            simbolodestino = "PEN"
            montofinal = montoinicial * tipocambio_penusd
        elif (monedadestino == 2): #USD
            simbolodestino = "USD"
            montofinal = montoinicial
        else: #EUR
            simbolodestino = "EUR"
            montofinal = montoinicial * tipocambio_penusd / tipocambio_peneur
    elif (monedaorigen == 3): #EUR
        simboloorigen = "EUR"
        if (monedadestino == 1): #PEN
            simbolodestino = "PEN"
            montofinal = montoinicial * tipocambio_peneur    
        elif (monedadestino == 2): #USD
            simbolodestino = "USD"
            montofinal = montoinicial * tipocambio_peneur / tipocambio_penusd
        else: #EUR
            simbolodestino = "USD"
            montofinal = montoinicial
        
#print("Monto " + montoinicial_string + " -> " + str(locale.currency(montofinal_number,True)))
#print("Monto " + montoinicial_string + " -> " + montofinal_string)
print("Conversión: ", "{:,.4f}".format(montoinicial), simboloorigen, " -> ", "{:,.4f}".format(montofinal), simbolodestino)
