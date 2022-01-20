from django.db import models

# Create your models here.
class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    
    def __str__(self):
        return self.nombre
    
class Receta(models.Model):
    titulo = models.CharField(max_length=100)
    ingredientes = models.TextField(help_text='Redacta los ingredientes')
    preparacion = models.TextField(help_text='Redacta cómo se prepara')
    tiempo_registro = models.DateTimeField(auto_now=True)
    autor = models.ForeignKey(Autor,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    receta = models.ForeignKey(Receta,on_delete=models.RESTRICT)
    texto = models.TextField(help_text='Escribe tu comentario')
    
    def __str__(self):
        return self.texto