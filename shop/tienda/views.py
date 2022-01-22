from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate

from .models import Categoria, Producto
from django.contrib.auth.models import User

from tienda.carrito import Cart
from tienda.forms import ClienteForm

# Create your views here.
def index(request):
    listaCategorias = Categoria.objects.all()
    listaProductos = Producto.objects.all()
    
    context = {
        'categorias': listaCategorias,
        'productos': listaProductos
    }
    return render(request,'index.html',context)

def productos_x_categoria(request,categoria_id):
    objCategoria = Categoria.objects.get(pk=categoria_id)
    lstCategorias = Categoria.objects.all()
    lstProductos = objCategoria.producto_set.all()
    context = {
        'categorias': lstCategorias,
        'productos': lstProductos
    }
    return render(request,'index.html',context)

def producto(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    context = {
        'producto': objProducto
    }
    return render(request,'producto.html',context)

def carrito(request):
    return render(request,'carrito.html')

def agregar_carrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    objCarritoProducto = Cart(request)
    objCarritoProducto.add(objProducto,1)
    return render(request,'carrito.html')

def eliminar_carrito(request,producto_id):
    objProducto = Producto.objects.get(pk=producto_id)
    objCarritoProducto = Cart(request)
    objCarritoProducto.remove(objProducto)
    return render(request,'carrito.html')

def limpiar_carrito(request):
    objCarritoProducto = Cart(request)
    objCarritoProducto.clear()
    return render(request,'carrito.html')

####################################################
# VISTAS PARA LOGIN Y REGISTRO DE USUARIOS
####################################################
def login_usuario(request): #Usamos este nombre para no entrar en conflicto con la palabra reservada 'login'
    context = {}
    if request.method == 'POST':
        dataUsuario = request.POST['usuario']
        dataPassword = request.POST['password']
        
        usuarioAuth = authenticate(request,username=dataUsuario,password=dataPassword)
        if usuarioAuth is not None:
            login(request,usuarioAuth)
            return redirect('/cuenta')
        else:
            context = {
                'error': 'datos incorrectos'
            }
            
    return render(request,'login.html')

def cuenta_usuario(request):
    clienteEditar = Cliente.objects.get(usuario = request.user)
    if clienteEditar.id is not None:
        dataCliente = {
            'nombres':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,
            'direccion':request.user.direccion,
            'telefono':request.user.telefono,
            'usuario':request.user.username
        }
    else:
        dataCliente = {
            'nombres':request.user.first_name,
            'apellidos':request.user.last_name,
            'email':request.user.email,
            'usuario':request.user.username
        }
    frmCliente = ClienteForm(dataCliente)
    
    context = {
        'frmCliente': frmCliente
    }
    return render(request,'cuenta.html',context)

def crear_usuario(request):
    if request.method == 'POST':
        dataUsuario = request.POST['nuevo_usuario']
        dataPassword = request.POST['nuevo_password']
        
        nuevoUsuario = User.objects.create_user(username=dataUsuario,password=dataPassword)
        login(request,nuevoUsuario)
        return redirect('/cuenta')
        