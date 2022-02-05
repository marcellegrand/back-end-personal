from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import *
from .serializers import *

# Create your views here.
class IndexView(APIView):
    def get(self, request):
        return Response({'status':'OK','content':'Running Server!'})

class PublicFavoriteAllView(APIView):
    def get(self, request):
        datos_Favorite = Favorite.objects.filter(scope='public')
        seria_Favorite = FavoriteSerializer(datos_Favorite,many=True)
        return Response(
            {'status':'OK','content':seria_Favorite.data}
        )
      
class FavoriteAllView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        datos_Favorite = Favorite.objects.all()
        seria_Favorite = FavoriteSerializer(datos_Favorite,many=True)
        return Response(
            {'status':'OK','content':seria_Favorite.data}
        )
        
    def post(self,request):
        seria_Favorite = FavoriteSerializer(data=request.data)
        seria_Favorite.is_valid(raise_exception=True)
        seria_Favorite.save()
        return Response(
            {'status':'OK','content':seria_Favorite.data}
        )
        
class FavoriteOneView(APIView):     
    permission_classes = [IsAuthenticated]
     
    def get(self,request,favorite_id):
        datos_Favorite = Favorite.objects.get(pk=favorite_id)
        seria_Favorite = FavoriteSerializer(datos_Favorite)
        return Response(
            {'status':'OK','content':seria_Favorite.data}
        )
        
    def put(self,request,favorite_id):
        datos_Favorite = Favorite.objects.get(pk=favorite_id)
        seria_Favorite = FavoriteSerializer(datos_Favorite,data=request.data)
        seria_Favorite.is_valid(raise_exception=True)
        seria_Favorite.save()
        return Response(
            {'status':'OK','content':seria_Favorite.data}
        )

    def delete(self,request,favorite_id):
        datos_Favorite = Favorite.objects.get(pk=favorite_id)
        seria_Favorite = FavoriteSerializer(datos_Favorite)
        datos_Favorite.delete()
        return Response(
            {'status':'OK','content':seria_Favorite.data}
        )
        
