from django.shortcuts import render

from .models import Categoria, Producto

# Create your views here.
def index(request):
    listaCategorias = Categoria.objects.all()
    listaProductos = Producto.objects.all()
    
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    return render(request,'index.html',context)