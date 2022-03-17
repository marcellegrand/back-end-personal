'''
Se recomienda, por buena práctica, empezar los nonbres de las clases en mayúsculas
La clase es un tipo de objeto; el objeto es la instancia de ese tipo
La función o método '__init__' es el constructor de la clase
El puntero 'self' hace referencia a la misma clase; una vez instanciada, al objeto
'''
class Automovil: 
    '''
    ATRIBUTOS (VARIABLES) DE CLASE
    Los valores aquí asignados los tendrán todos los objetos instanciados
    '''
    kind = 'Transportation' #Atributo NO MUTABLE
    surfaces = ['land','pavement','road'] #Atributo MUTABLE
    
    def __init__(self,year,register,colour,brand,model):
        '''
        ATRIBUTOS (VARIABLES) DE OBJETO
        Los valores aquí asignados los tendrá únicamente el objeto instanciado
        '''        
        self.year = year
        self.register = register
        self.colour = colour
        self.brand = brand
        self.model = model
        self.cylinder = 1000
        
    def encender(self):
        print('encender ' + self.brand + ' ' + self.model)
    def avanzar(self):
        print('avanzar ' + self.brand + ' ' + self.model)
    def acelerar(self):
        print('acelerar ' + self.brand + ' ' + self.model)
    def frenar(self):
        print('frenar ' + self.brand + ' ' + self.model)

#OBJETO: Volkswagen Escarabajo
vw_es = Automovil(1970,'CH-1234','Amarillo','Volkswagen','Escarabajo')
#OBJETO: Audi S3
audi_s3 = Automovil(2020,'HQ-5854','Rojo','Audi','S3')

vw_es.encender() 
vw_es.acelerar()
vw_es.frenar()
 
audi_s3.encender()  
audi_s3.acelerar()
audi_s3.frenar()

'''ATRIBUTOS DE CLASE'''
vw_es.kind = 'Transportation media' #NO MUTABLE
print(audi_s3.kind)
print(vw_es.kind)

audi_s3.surfaces.append('highway') #MUTABLE
print(audi_s3.surfaces)
print(vw_es.surfaces)

'''ATRIBUTOS DE OBJETO'''
vw_es.colour = "Verde"
print(vw_es.colour)
print(audi_s3.colour)

audi_s3.year = 2022
print(audi_s3.year)
print(vw_es.year)

'''
BORRANDO UN ATRIBUTO DE CLASE
El atributo de clase NO MUTABLE no se borra. Se borra el valor que se le haya asignado
El atributo de clase MUTABLE no puede intentar borrarse con 'del'.
''' 
print(audi_s3.kind)
del vw_es.kind
print('Limpiando el atributo de clase NO MUTABLE')
print(vw_es.kind)

try:
    del audi_s3.surfaces
except:
     print('Imposible borrar un atributo de clase MUTABLE')

'''
BORRANDO UN ATRIBUTO DE OBJETO
'''
try:
    print(vw_es.colour)
    del audi_s3.colour
    print(audi_s3.colour)
except:
    print('Atributo de objeto no definido en el objeto')
    

        
    