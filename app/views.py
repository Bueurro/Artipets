from django.http import request
from django.shortcuts import render
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
    return render(request,'app/comidas.html')

def comidasnl(request):
    return render(request,'app/comidasnl.html')

def correas(request):
    return render(request,'app/correas.html')

def correasnl(request):
    return render(request,'app/correasnl.html')

def identificaciones(request):
    return render(request,'app/identificaciones.html')

def identificacionesnl(request):
    return render(request,'app/identificacionesnl.html')

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
            
    return render(request,'app/agregar_producto.html',datos)       