from rest_framework import serializers
from .models import Cliente
from django.contrib.auth.models import User

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name')
        #Con esto NO mostraremos el password 
        extra_kwargs = {'password':{'write_only':True}}
    
    """
    Este método es el invocado por el save()
    Acá lo estamos redefiniendo para almacenar 
    el password de forma encriptada
    """
    def create(self,validated_data):
        nuevo_usuario = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        nuevo_usuario.set_password(validated_data['password'])
        nuevo_usuario.save()
        
        return nuevo_usuario

class ClienteRegistroSerializer(serializers.ModelSerializer):
    identity = serializers.CharField(max_length = 8)
    address = serializers.CharField()
    
    class Meta:
        model = User
        fields = ('username','password','email','first_name','last_name','identity','address')
        #Con esto NO mostraremos el password 
        extra_kwargs = {'password':{'write_only':True}}    

    """
    Este método es el invocado por el save()
    Acá lo estamos redefiniendo para almacenar 
    el password de forma encriptada
    """        
    def create(self,validated_data):
        nuevo_usuario = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        
        nuevo_usuario.set_password(validated_data['password'])
        nuevo_usuario.save()
        
        nuevo_cliente = Cliente.objects.create(
            user=nuevo_usuario,
            identity=validated_data['identity'],
            address=validated_data['address']
        )
        
        nuevo_cliente_dicc = {
            'cliente_id':nuevo_cliente.id
        }
        
        return nuevo_cliente_dicc

class UsuarioLoginSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls,user):
        token = super(UsuarioLoginSerializer,cls).get_token(user)
        
        token['username'] = user.username
        return token 
    
    def validate(self, attrs):
        data = super().validate(attrs)
        refresh = self.get_token(self.user)
        
        data["refresh"] = str(refresh)
        data["token"] = str(refresh.access_token)
        data["user"] = str(self.user.username)
        
        if api_settings.UPDATE_LAST_LOGIN:
            update_last_login(None, self.user)
            
        return data