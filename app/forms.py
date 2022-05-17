from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *

#creamos un template del formulario

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5,max_length=60)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = ['plu_codigo','stock','precio','preciooferta','nombre','marca','descripcion','tipo','imagen']
   
class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['id_usuario','usuario','nombre','apellido','correo','direccion','contrasena','confirmar_contrasena']