from django.http import request
from django.shortcuts import render, redirect
from .models import *
from .forms import *

#Indexs / login

def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/index.html',datos)
    
def login(request):
    return render(request,'app/login.html')

def homelogin(request):
    return render(request,'app/homelogin.html')


#Navbar

def bandanas(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/bandanas.html',datos)

def bandanasnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/bandanasnl.html',datos)

def comidas(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/comidas.html',datos)

def comidasnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/comidasnl.html',datos)

def correas(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/correas.html',datos)

def correasnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/correasnl.html',datos)

def identificaciones(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/identificaciones.html',datos)

def identificacionesnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/identificacionesnl.html',datos)

#logOptions

def carrito(request):
    return render(request,'app/carrito.html')

def historial(request):
    return render(request,'app/historial.html')

def suscripcion(request):
    return render(request,'app/suscripcion.html')

#plushtmls

def agregar_producto(request):
    return render(request,'app/agregar_producto.html')


def agregar_producto(request):
    #return render(request,'app/agregar_producto.html')
    datos = {'form' : ProductoForm()}

    if request.method == 'POST' :
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente!"
            
    return render(request,'app/productos/agregar_producto.html',datos)

def modificar_producto(request,plu_codigo):
    producto = Producto.objects.get(plu_codigo=plu_codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }

    if request.method == 'POST' :
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente!"
            datos['form'] = formulario
            
    return render(request,'app/productos/modificar_producto.html',datos)

def listar_productos(request):
    datos = {'form' : ProductoForm()}
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
            
    return render(request,'app/productos/listar_productos.html',datos)


def eliminar_producto(request, plu_codigo):
    producto = Producto.objects.get(plu_codigo=plu_codigo)
    producto.delete()

    return redirect(to="listar_productos")