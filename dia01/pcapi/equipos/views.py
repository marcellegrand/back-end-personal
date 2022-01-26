# from django.shortcuts import render
# Hemos comentado la línea anterior porque acá no vamos a renderizar absolutamente nada
# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Empleado, Equipo
from .serializers import EmpleadoSerializer, EquipoSerializer

@api_view(['GET'])
def index(request):
    data = {'mensaje':'Hola mundo json'}
    return Response(data)

@api_view(['GET'])
def listar_empleados(request):
    lstEmpleados = Empleado.objects.all()
    
    #Convertir el QuerySet a un formato json: Primera forma
    #dataEmpleados = [] #Inicializando un arreglo vacío
    #for rcdEmpleado in lstEmpleados:
    #    dataEmpleados.append({
    #            'nombre':rcdEmpleado.nombre,
    #            'email':rcdEmpleado.email
    #    })
    #return Response({'status':'OK','empleados':dataEmpleados})
    
    #Convertir el QuerySet a un formato json: Serializer
    seriEmpleados = EmpleadoSerializer(lstEmpleados,many=True)
    return Response({'status':'OK','empleados':seriEmpleados.data})
    

@api_view(['POST'])
def crear_empleado(request):
    #Guardando los datos: Primera forma
    #objEmpleado = Empleado()
    #objEmpleado.nombre = request.data['nombre']
    #objEmpleado.email = request.data['email']
    #objEmpleado.save()
    #
    #dataEmpleado = {
    #    'id':objEmpleado.id,
    #    'nombre':objEmpleado.nombre,
    #    'email':objEmpleado.email
    #}
    
    #Guardando los datos: Serializer
    seriEmpleado = EmpleadoSerializer(data=request.data)
    seriEmpleado.is_valid(raise_exception=True)
    #objEmpleado = seriEmpleado.save()
    seriEmpleado.save()
    
    #return Response({'status':'OK','empleado':EmpleadoSerializer(objEmpleado).data})
    return Response({'status':'OK','empleado':seriEmpleado.data})

@api_view(['GET','POST'])
def equipos(request):
    if request.method == 'GET':
        #Retornar los equipos
        lstEquipos = Equipo.objects.all()        
        seriEquipos = EquipoSerializer(lstEquipos,many=True)
        return Response({'status':'OK','equipos':seriEquipos.data})
    elif request.method == 'POST':
        #Guardar un equipo
        seriEquipo = EquipoSerializer(data=request.data)
        if seriEquipo.is_valid():
            seriEquipo.save()
            return Response({'status':'OK','equipo':seriEquipo.data})
        else:
            return Response(seriEquipo.errors)
        
        
        