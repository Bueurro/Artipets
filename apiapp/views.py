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

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class SuscriptorViewSet(viewsets.ModelViewSet):
    queryset = Suscriptor.objects.all()
    serializer_class = SuscriptorSerializer
