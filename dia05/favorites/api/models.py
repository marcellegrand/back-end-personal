from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Favorite(models.Model):
    PRIVATE = 'private'
    PUBLIC = 'public'
    
    SCOPE_CHOICES = (
        (PRIVATE,'Privado'),
        (PUBLIC,'Público')
    )
    
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=500)
    created = models.DateField()
    scope = models.CharField(max_length=10,choices=SCOPE_CHOICES)
    user = models.ForeignKey(User,on_delete=models.RESTRICT)
    
    def __str__(self):
        return self.name 