#from django.shortcuts import render
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
class IndexView(APIView):
    def get(self,request):
        context = {
            'active':True,
            'message':'Running server!'
        }
        return Response(context)

class CategoriaView(APIView):
    
    def get(self,request):
        dataCategorias = Categoria.objects.all()
        seriCategorias = CategoriaSerializer(dataCategorias,many=True)
        
        return Response({'status':True,'content':seriCategorias.data})

    def post(self,request):
        seriCategoria = CategoriaSerializer(data=request.data)
        seriCategoria.is_valid(raise_exception=True)
        seriCategoria.save()
        
        return Response({'status':True,'content':seriCategoria.data})

class MesaView(APIView):
    
    def get(self,request):
        dataMesas = Mesa.objects.all()
        seriMesas = MesaSerializer(dataMesas,many=True)
        
        return Response({'status':True,'content':seriMesas.data})

    def post(self,request):
        seriMesa = MesaSerializer(data=request.data)
        seriMesa.is_valid(raise_exception=True)
        seriMesa.save()
        
        return Response({'status':True,'content':seriMesa.data})

class PlatoView(APIView):
    
    def get(self,request):
        dataPlatos = Plato.objects.all()
        seriPlatos = PlatoSerializer(dataPlatos,many=True)
        
        return Response({'status':True,'content':seriPlatos.data})

    def post(self,request):
        seriPlato = PlatoSerializer(data=request.data)
        seriPlato.is_valid(raise_exception=True)
        seriPlato.save()
        
        return Response({'status':True,'content':seriPlato.data})
    
class CategoriaPlatosView(APIView):
    
    def get(self,request,categoria_id):
        dataCategoria = Categoria.objects.get(pk=categoria_id)
        seriCategoriaPlatos = CategoriaPlatosSerializer(dataCategoria)
        context = {
            'status':True,
            'content':seriCategoriaPlatos.data
        }
        
        return Response(context)
        
