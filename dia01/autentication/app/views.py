from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

#Librerías propias para la autenticación
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

class IndexView(APIView):
    
    #Con esto restringimos que solo se pueda usar con autenticación
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        context = {
            'status':True,
            'content':'running server!',
            'user':str(request.user)
        }
        return Response(context)