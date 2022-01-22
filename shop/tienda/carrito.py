class Cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart") #Obteniendo una variable de sesión
        if not cart:
            cart = self.session["cart"] = {} #Creando un diccionario vacío
        
        self.cart = cart
        
    def add(self,producto,quantity):
        if str(producto.id) not in self.cart.keys():
            self.cart[producto.id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "cantidad": quantity,
                "precio": str(producto.precio),
                "imagen": producto.imagen.url,
                "total": str(quantity * producto.precio)
            }
        else:
            for key,value in self.cart.items():
                if key == str(producto.id):
                    value["cantidad"] = str(int(value["cantidad"]) + quantity)
                    value["total"] = str(float(value["cantidad"]) * float(value["precio"]))
                    break
                    
        self.save()
    
    def save(self):
        self.session["cart"] = self.cart 
        self.session.modified = True
           
    def remove(self,producto):
        producto_id = str(producto.id)
        if producto_id in self.cart:
            del self.cart[producto_id]
            self.save()
    
    def clear(self):
        self.session["cart"] = {}