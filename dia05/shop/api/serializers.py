from tienda.models import *
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['imagen'] = instance.imagen.url
        return representation        
        
class CategoriaProductoSerializer(serializers.ModelSerializer):
    Productos = ProductoSerializer(many=True,read_only=True)
    class Meta:
        model = Categoria
        fields = ['id','nombre','Productos']
    
        