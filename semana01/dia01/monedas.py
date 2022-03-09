##############################################
#CONVERSOR DE MONEDAS
##############################################

#ZONA DE IMPORTACIÓN
import locale
import os

#CONFIGURACIONES BÁSICAS
locale.setlocale(locale.LC_ALL,'es_PE.UTF-8')

#DEFINICIÓN DE VARIABLES
dicFactores = []
tipocambio_penusd = 0
tipocambio_peneur = 0
indice = 0
clave = ''
valor = ''
tupla = 1

monedaorigen = 0
monedadestino = 0
simboloorigen = "PEN"
simbolodestino = "PEN"
montoinicial = 0
montofinal = 0
reintentarmonedas = True
reintentarmonto = True

#APERTURA DEL ARCHIVO DE FACTORES DE CAMBIO
if (os.path.isfile('factores.txt')):
    filFactores = open('factores.txt','r')
    strFactores = filFactores.read()
    #penusd->3.780
    #peneur->4.570
    arrFactores = strFactores.splitlines()
    #['penusd->3.780', 'peneur->4.570']
    
    for eleFactor in arrFactores:
        comFactor = eleFactor.split('->')
        #penusd
        #3.780
        #peneur
        #4.570
        dicFactor = {
            'key':comFactor[0],
            'value':comFactor[1]
        }
        dicFactores.append(dicFactor)
    
    filFactores.close()

#SETEO DE FACTORES DE CAMBIO
indice = 0
while (indice < len(dicFactores)):
    tupla = 1
    for clave, valor in dicFactores[indice].items():
        if (tupla == 2):
            if (indice == 0): #PEN->USD
                tipocambio_penusd = float(valor)
            if (indice == 1): #PEN->EUR
                tipocambio_peneur = float(valor)
        tupla+=1 #tupla = tupla + 1
    indice+=1 #indice = indice + 1

#INICIO DEL PROGRAMA
print("Monedas:")
print("(1) PEN")
print("(2) USD")
print("(3) EUR")

#montoinicial_number = float(input("Monto inicial: "))
#montoinicial_string = "$ {:,.2f}".format(montoinicial_number)
#montofinal_number = montoinicial_number * tipocambio 
#montofinal_string = "S/ {:,.2f}".format(montofinal_number)

while (reintentarmonedas):
    monedaorigen = int(input("Moneda ORIGEN: "))
    monedadestino = int(input("Moneda DESTINO: "))
    
    if (monedaorigen < 1 or monedaorigen > 3 or monedadestino < 1 or monedadestino > 3):
        reintentarmonedas = True
    else:
        reintentarmonedas = False
        
        while (reintentarmonto):
            montoinicial = float(input("Monto ORIGEN: "))
            
            if (montoinicial == 0):
                reintentarmonto = True
            else:
                reintentarmonto = False
                
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
