from django.shortcuts import render
from rest_framework import viewsets
from app.models import *
from .serializers import *


# Create your views here.

# SE ENCARGA DE MOSTRAR LA DATA  EN EL API
class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
class TipoProductoViewSet(viewsets.ModelViewSet):
    queryset = TipoProducto.objects.all()
    serializer_class = TipoProductoSerializer

