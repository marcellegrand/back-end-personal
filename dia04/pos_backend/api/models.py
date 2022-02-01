from django.db import models

#Importamos la tabla de usuarios propia del modelo de django
from django.contrib.auth.models import User

from cloudinary.models import CloudinaryField

# Create your models here.
class Categoria(models.Model):
    categoria_id = models.AutoField(primary_key=True) #Para definir una PK
    categoria_nom = models.CharField(max_length=100,verbose_name='nombre') #Se usa el verbose como alias o tag del campo
    
    def __str__(self):
        return self.categoria_nom
    
class Plato(models.Model):
    plato_id = models.AutoField(primary_key=True)
    plato_nom = models.CharField(max_length=200,verbose_name='nombre del plato')
    plato_img = CloudinaryField('image',default='')
    plato_pre = models.DecimalField(max_digits=10,decimal_places=2,default=0,verbose_name='precio')
    categoria_id = models.ForeignKey(
            Categoria,
            related_name='Platos', #Nombre con el cual desde la tabla padre podemos traer todos los datos relacionados en la tabla hija
            to_field='categoria_id', #Campo en la tabla padre
            on_delete=models.RESTRICT,
            db_column='categoria_id', #Campo en esta tabla (tabla hija)
            verbose_name='categoria'
        )
    
    def __str__(self):
        return self.plato_nom
    
class Mesa(models.Model):
    mesa_id = models.AutoField(primary_key=True)
    mesa_nro = models.CharField(max_length=10,verbose_name='mesa nro')
    mesa_cap = models.IntegerField(default=0,verbose_name='capacidad')

    def __str__(self):
        return self.mesa_nro
    
class Pedido(models.Model):
    pedido_id = models.AutoField(primary_key=True)
    pedido_fech = models.DateTimeField(null=True,verbose_name='fecha')
    pedido_nro = models.CharField(max_length=100,default='',verbose_name='pedido nro')
    pedido_est = models.CharField(max_length=100,default='pagado',verbose_name='Estado')
    
    usu_id = models.ForeignKey(
            User,
            related_name='PedidoUsuario', #Nombre con el cual desde la tabla padre podemos traer todos los datos relacionados en la tabla hija
            to_field='id', #Campo en la tabla padre
            on_delete=models.RESTRICT,
            db_column='usu_id', #Campo en esta tabla (tabla hija)
            verbose_name='usuario'
        )
    
    mesa_id = models.ForeignKey(
            Mesa,
            related_name='PedidoMesa', #Nombre con el cual desde la tabla padre podemos traer todos los datos relacionados en la tabla hija
            to_field='mesa_id', #Campo en la tabla padre
            on_delete=models.RESTRICT,
            db_column='mesa_id', #Campo en esta tabla (tabla hija)
            verbose_name='mesa'
    )
    
class PedidoPlato(models.Model):
    pedidoplato_id = models.AutoField(primary_key=True)
    pedidoplato_cant = models.IntegerField(default=1,verbose_name='cantidad')

    pedido_id = models.ForeignKey(
            Pedido,
            related_name='pedidoplatos', #Nombre con el cual desde la tabla padre podemos traer todos los datos relacionados en la tabla hija
            to_field='pedido_id', #Campo en la tabla padre
            on_delete=models.RESTRICT,
            db_column='pedido_id', #Campo en esta tabla (tabla hija)
            verbose_name='pedido'
    ) 
        
    plato_id = models.ForeignKey(
            Plato,
            related_name='pedidoplatos', #Nombre con el cual desde la tabla padre podemos traer todos los datos relacionados en la tabla hija
            to_field='plato_id', #Campo en la tabla padre
            on_delete=models.RESTRICT,
            db_column='plato_id', #Campo en esta tabla (tabla hija)
            verbose_name='plato'
    ) 