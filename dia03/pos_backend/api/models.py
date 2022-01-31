from django.db import models

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
            related_name='Platos',
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