from rest_framework import serializers
from app.models import *
from app.views import suscripcion


# SE ENCARGA DE HACER EL CRUD DESDE EL API
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class SuscriptorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscriptor
        fields = '__all__'