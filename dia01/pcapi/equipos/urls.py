from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('empleados/listar',views.listar_empleados,name='listar_empleados'),
    path('empleados/crear',views.crear_empleado,name='crear_empleado'),
    path('equipos',views.equipos,name='equipos')
]