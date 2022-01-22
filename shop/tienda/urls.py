from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('',views.index,name='index'),
    path('productos_x_categoria/<int:categoria_id>',views.productos_x_categoria,name='productos_x_categoria'),
    path('producto/<int:producto_id>',views.producto,name='producto'),
    path('carrito',views.carrito,name='carrito'),
    path('agregar_carrito/<int:producto_id>',views.agregar_carrito,name='agregar_carrito'),
    path('eliminar_carrito/<int:producto_id>',views.eliminar_carrito,name='eliminar_carrito'),
    path('limpiar_carrito/',views.limpiar_carrito,name='limpiar_carrito'),
    
    # RUTAS PARA LOGIN Y REGISTRO DE USUARIOS
    path('login',views.login_usuario,name='login_usuario'),
    path('cuenta',views.cuenta_usuario,name='cuenta_usuario'),
    path('crear_usuario',views.crear_usuario,name='crear_usuario')
]