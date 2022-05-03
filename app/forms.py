from django import forms
from django.forms import ModelForm
from .models import *

#creamos un template del formulario

class ProductoForm(ModelForm):

    class Meta:
        model = Producto
        fields = ['plu_codigo','nombre','marca','precio','stock','descripcion','tipo']