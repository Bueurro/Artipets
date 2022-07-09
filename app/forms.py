from dataclasses import fields
from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


#creamos un template del formulario
class RegistroUsuarioForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1','password2']
        #buscar siempre la base de datos con el sqlite

class ProductoForm(ModelForm):

    nombre = forms.CharField(min_length=5,max_length=60)
    precio = forms.IntegerField(min_value=400)

    class Meta:
        model = Producto
        fields = '__all__'
        
class UsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields = '__all__'

class PedidoForm(ModelForm):

    class Meta:
        model = Pedido
        fields = ['codigo','estado']