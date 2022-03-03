from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from rest_framework.permissions import IsAuthenticated
 
from .models import Cliente
from django.contrib.auth.models import User

from .serializers import UsuarioSerializer, ClienteRegistroSerializer, UsuarioLoginSerializer

# Create your views here.
class indexView(APIView):
    def get(self,request):
        context = {
            'status':True,
            'content':'API running succesfully!'
        }
        
        return Response(context)

class UsuarioLoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = UsuarioLoginSerializer
    
class UsuarioView(APIView):
    def get(self,request):
        usuario_data = User.objects.all()
        usuario_seri = UsuarioSerializer(usuario_data,many=True)
        context = {
            'status':True,
            'content':usuario_seri.data
        } 
        return Response(context)
    
    def post(self,request):
        usuario_seri = UsuarioSerializer(data=request.data)
        usuario_seri.is_valid(raise_exception = True)
        usuario_seri.save()
        
        context = {
            'status':True,
            'content':usuario_seri.data
        }
        return Response(context)
    
class ClienteRegistroView(APIView):
    def post(self,request):
        cliente_seri = ClienteRegistroSerializer(data=request.data)
        cliente_seri.is_valid(raise_exception = True)
        cliente_seri.save()
        
        context = {
            'status':True,
            'content':cliente_seri.data
        }
        return Response(context)
        
        