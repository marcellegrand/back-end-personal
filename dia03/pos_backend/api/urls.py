from django.urls import path
from . import views

urlpatterns = [
    path('',views.IndexView.as_view(),name='IndexView'),
    path('categoria',views.CategoriaView.as_view(),name='CategoriaView'),
    path('mesa',views.MesaView.as_view(),name='MesaView'),
    path('plato',views.PlatoView.as_view(),name='PlatoView'),
    path('categoria/<int:categoria_id>/platos',views.CategoriaPlatosView.as_view(),name='CategoriaPlatosView'),
    path('pedido',views.PedidoView.as_view(),name='Pedido')
]