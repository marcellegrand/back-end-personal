from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Serie
from .serializers import SerieSerializer

# Create your views here.
class IndexView(APIView):
    def get(self,request):
        context = {'mensaje':'servidor activo'}
        return Response(context)

class SeriesView(APIView):
    
    def get(self,request):
        dataSeries = Serie.objects.all()
        seriSeries = SerieSerializer(dataSeries,many=True)
        
        return Response(seriSeries.data)

    def post(self,request):
        seriSerie = SerieSerializer(data=request.data)
        seriSerie.is_valid(raise_exception=True)
        seriSerie.save()
        
        return Response(seriSerie.data)

class SerieDetailView(APIView):
    def get(self,request,serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        seriSerie = SerieSerializer(dataSerie)
        
        return Response(seriSerie.data)
    
    def put(self,request,serie_id):
        dataSerie = Serie.objects.get(pk=serie_id)
        seriSerie = SerieSerializer(dataSerie,data=request.data)
        seriSerie.is_valid(raise_exception=True)
        seriSerie.save()
        
        return Response(seriSerie.data)
        
    def delete(self,request,serie_id):
        objeSerie = Serie.objects.get(pk=serie_id)
        seriSerie = SerieSerializer(objeSerie)
        objeSerie.delete()
        
        #return Response({'deleted_status':'ok'})
        return Response(seriSerie.data)
        
        
