class Empresa:
    def __init__(self,ruc,razonsocial,telefono,email):
        self.ruc = ruc
        self.razonsocial = razonsocial
        self.telefono = telefono
        self.email = email
    def mostrar(self):
        return str(self.ruc) + ';' + self.razonsocial + ';' + str(self.telefono) + ';' + self.email


class Cliente(Empresa):
    def __init__(self,ruc,razonsocial,telefono,email,credito):
        super().__init__(ruc,razonsocial,telefono,email)   
        self.credito = credito
    def mostrar(self):
        return super().mostrar() + ';' + str(self.credito)
        

class Proveedor(Empresa):
    def __init__(self,ruc,razonsocial,telefono,email,calificacion):
        super().__init__(ruc,razonsocial,telefono,email)   
        self.calificacion = calificacion
    def mostrar(self):
        return super().mostrar() + ';' + str(self.calificacion)
    

michell = Empresa(20100192650,'Michell',125456789,'michell@michell.com.pe')
print(michell.mostrar())

mfh = Proveedor(201002569874,'MFH',987654321,'mfh@mfh.com.pe',1000)
print(mfh.mostrar())

incalpaca = Cliente(20100478569,'INCALPACA',741852963,'incalpaca@grupoinca.com',1000000)
print(incalpaca.mostrar())