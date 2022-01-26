from rest_framework import serializers
from .models import Empleado, Equipo

class EmpleadoSerializer(serializers.Serializer):
    nombre = serializers.CharField()
    email = serializers.EmailField()
    
    def create(self,validated_data):
        #Se destructura la data de validated_data, por eso se manda con **
        #El método create de la clase Empleado.objects recibe datos destructurados
        #Estructurado: {'nombre':'<name>','email':'<email>'}
        #Destructurado: nombre='<name>',email='<email>'
        return Empleado.objects.create(**validated_data)
    
class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'
        
    #Con las líneas anteriores evitamos todas las demás de abajo
    #marca = serializers.CharField()
    #serie = serializers.CharField()
    #modelo = serializers.CharField()
    #procesador = serializers.CharField()
    #memoria = serializers.IntegerField()
    #disco = serializers.IntegerField()
    
    def create(self,validated_data):
        return Equipo.objects.create(**validated_data)
    
    