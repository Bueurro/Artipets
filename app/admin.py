from encodings import search_function
from re import search
from django.contrib import admin
from .models import *

# Register your models here.

#Crear las columnas para que el admin vea los productos ordenados
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['codigo','stock','precio','nombre','marca','tipo'] #mostrar el producto ordenado por sus caracteristicas
    search_fields =['codigo','nombre'] #Un buscador que segun el parametro va ser por lo que busquemos
    list_per_page = 3 # son los productos que se muestran por pagina


admin.site.register(TipoProducto) #esto sirve para que se visualice en el modo admin 
admin.site.register(Producto,ProductoAdmin)

