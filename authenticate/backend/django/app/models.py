from django.db import models

from django.contrib.auth.models import User

# Create your models here.
class Cliente(models.Model):
    user = models.OneToOneField(User,on_delete=models.RESTRICT)
    identity = models.CharField(max_length=8)
    address = models.TextField()
    
    def __str__(self):
        return self.identity