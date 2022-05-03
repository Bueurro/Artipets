from django.shortcuts import render
from .models import *
from .forms import *

#Indexs / login

def index(request):
    return render(request,'app/index.html')
    productosAll = Productos.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    
def login(request):
    return render(request,'app/login.html')

def homelogin(request):
    return render(request,'app/homelogin.html')


#Navbar

def bandanas(request):
    return render(request,'app/bandanas.html')

def bandanasnl(request):
    return render(request,'app/bandanasnl.html')

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
