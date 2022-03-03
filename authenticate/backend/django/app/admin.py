from django.contrib import admin

from .models import Cliente

# Register your models here.

#Forma estándar de registrar el modelo.
#admin.site.register(Cliente)

#Forma personalizada de registrar el modelo.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('identity','user','address')
