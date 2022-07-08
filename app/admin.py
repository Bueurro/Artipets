from encodings import search_function
from re import search
from django.contrib import admin
from .models import *

# Register your models here.

#Crear las columnas para que el admin vea los productos ordenados
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['plu_codigo','stock','precio','preciooferta','nombre','marca','descripcion','tipo','imagen'] #mostrar el producto ordenado por sus caracteristicas
    search_fields =['plu_codigo','nombre'] #Un buscador que segun el parametro va ser por lo que busquemos
    list_per_page = 5 # son los productos que se muestran por pagina



class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario','nombre','apellido','correo','direccion'] #mostrar el producto ordenado por sus caracteristicas
    search_fields =['usuario'] #Un buscador que segun el parametro va ser por lo que busquemos
    list_per_page = 5 # son los productos que se muestran por pagina




admin.site.register(TipoProducto) #esto sirve para que se visualice en el modo admin 
admin.site.register(Producto,ProductoAdmin)
admin.site.register(Carrito_Producto)
admin.site.register(Usuario,UsuarioAdmin)