class Automovil: #Se recomienda, por buena práctica, empezar las clases en mayúsculas
    def __init__(self,year,register,colour,brand,model):
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

vw_es = Automovil(1970,'CH-1234','Amarillo','Volkswagen','Escarabajo')
audi_s3 = Automovil(2020,'HQ-5854','Rojo','Audi','S3')

vw_es.encender()
audi_s3.acelerar()    

del audi_s3.colour
print(audi_s3.colour)

        
    