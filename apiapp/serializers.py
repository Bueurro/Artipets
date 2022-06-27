from rest_framework import serializers
from app.models import *


# SE ENCARGA DE HACER EL CRUD DESDE EL API
class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = '__all__'
        
class TipoProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields = '__all__'