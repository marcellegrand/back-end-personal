from rest_framework import serializers

from .models import Categoria, Plato, Mesa, Pedido, PedidoPlato

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'
        
class PlatoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plato
        fields = '__all__'
    
    #Sobreescribiendo esta función
    def to_representation(self,instance):
        representation = super().to_representation(instance)
        representation['plato_img'] = instance.plato_img.url
        return representation

class MesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mesa
        fields = '__all__'

class CategoriaPlatosSerializer(serializers.ModelSerializer):
    Platos = PlatoSerializer(many=True,read_only=True)
    
    class Meta:
        model = Categoria
        fields = ['categoria_id','categoria_nom','Platos']  
      
class PedidoPlatoSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['plato_id','pedidoplato_cant']          
          
class PedidoSerializerPOST(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerPOST(many=True)
    
    class Meta:
        model = Pedido
        fields = ['pedido_fech','pedido_nro','pedido_est','usu_id','mesa_id','pedidoplatos'] 
    
    def create(self,validated_data):
        pedidos_data = validated_data.pop('pedidoplatos') #Cogiendo el valor de PedidoPlatos y eliminándolo de validated_data
        pedido = Pedido.objects.create(**validated_data)
        for pedido_data in pedidos_data:
            PedidoPlato.objects.create(pedido_id=pedido,**pedido_data)
        
        return pedido

class PedidoPlatoSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = PedidoPlato
        fields = ['pedidoplato_id','pedidoplato_cant','plato_id','pedido_id'] 
        
class PedidoSerializerGET(serializers.ModelSerializer):
    pedidoplatos = PedidoPlatoSerializerGET(many=True,read_only=True)
    
    class Meta:
        model = Pedido
        fields = ['pedido_id','pedido_fech','pedido_nro','pedido_est','mesa_id','usu_id','pedidoplatos']