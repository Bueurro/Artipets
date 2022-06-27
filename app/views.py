from calendar import c
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from app.forms import ProductoForm
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
import requests
#---------------------
from pickle import TRUE
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
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

@login_required 
def homelogin(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }    
    return render(request,'app/homelogin.html',datos)

#Navbar
@login_required 
def bandanas(request):
    
    productosAll = Producto.objects.all()
    datos = { 
        'listaProductos' : productosAll,
        }
    
    if request.method == 'POST':
        tipoProducto = TipoProducto()
        tipoProducto.tipo = request.POST.get('tipo')

        producto = Producto()
        producto.plu_codigo = request.POST.get('codigo_producto')
        producto.stock = request.POST.get('stock_producto')
        producto.precio = request.POST.get('precio_producto')
        producto.preciooferta = request.POST.get('preciooferta')         
        producto.nombre = request.POST.get('nombre_producto')      
        producto.marca = request.POST.get('marca_producto')  
        producto.descripcion = request.POST.get('descripcion')
        producto.imagen = request.POST.get('imagen_producto')
        producto.tipo = tipoProducto

        carrito = Carrito_Producto()
        carrito.plu_codigo = producto
        carrito.save()
        messages.success(request,'Producto guardado correctamente!')

        plu_codigo = request.POST.get('codigo_producto')
        productoA = Producto.objects.get(plu_codigo=plu_codigo)
        productoA.stock -= 1
        productoA.save()
        messages.success(request,'Producto Enviado al carrito correctamente!')
        
    return render(request, 'app/bandanas.html', datos)

def bandanasnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/bandanasnl.html',datos)
@login_required 
def comidas(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        
        carrito = Carrito_Producto()
        carrito.nombre_producto = request.POST.get('nombre_producto')      
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.preciooferta = request.POST.get('preciooferta')
        carrito.descripcion = request.POST.get('descripcion')
        carrito.imagen = request.POST.get('imagen_producto')  
        carrito.save()

        plu_codigo = request.POST.get('codigo_producto')
        productoA = Producto.objects.get(plu_codigo=plu_codigo)
        productoA.stock -= 1
        productoA.save()
        messages.success(request,'Producto Enviado al carrito correctamente!')

    return render(request,'app/comidas.html',datos)

def comidasnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/comidasnl.html',datos)

@login_required 
def correas(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        carrito = Carrito_Producto()
        carrito.nombre_producto = request.POST.get('nombre_producto')      
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.preciooferta = request.POST.get('preciooferta')
        carrito.descripcion = request.POST.get('descripcion')
        carrito.imagen = request.POST.get('imagen_producto')  
        carrito.save()


        plu_codigo = request.POST.get('codigo_producto')
        productoA = Producto.objects.get(plu_codigo=plu_codigo)
        productoA.stock -= 1
        productoA.save()
        messages.success(request,'Producto Enviado al carrito correctamente!')

    return render(request,'app/correas.html',datos)

def correasnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/correasnl.html',datos)

@login_required 
def identificaciones(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }

    if request.method == 'POST':
        carrito = Carrito_Producto()
        carrito.nombre_producto = request.POST.get('nombre_producto')      
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.preciooferta = request.POST.get('preciooferta')
        carrito.descripcion = request.POST.get('descripcion')
        carrito.imagen = request.POST.get('imagen_producto')  
        carrito.save()


        plu_codigo = request.POST.get('codigo_producto')
        productoA = Producto.objects.get(plu_codigo=plu_codigo)
        productoA.stock -= 1
        productoA.save()
        messages.success(request,'Producto Enviado al carrito correctamente!')

    return render(request,'app/identificaciones.html',datos)

def identificacionesnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/identificacionesnl.html',datos)

#logOptions

@permission_required('app.view_carrito_producto') #LISTO
def carrito(request):

    carritoAll = Carrito_Producto.objects.all()
       
    datos = { 'listacarrrito' : carritoAll,
                 
    
    # hacer un if para mostrar el permiso de si esta suscrtito para mostrar el total con descuento o el total normalito 
    'Total': round(sum(c.plu_codigo.precio for c in carritoAll)),
    'descuento_suscriptor': round(sum(c.plu_codigo.precio*0.05 for c in carritoAll)),
    'TotalPagar': round(sum(c.plu_codigo.precio - c.plu_codigo.precio*0.05 for c in carritoAll)),
    
    }

    return render(request, 'app/carrito.html',datos)

@permission_required('app.view_carrito_producto')
def eliminar_carrito(request, id):
    productocarro = Carrito_Producto.objects.get(id=id)
    productocarro.delete()

    return redirect(to="carrito")


@login_required 
def pagar(request):
    carritoall = Carrito_Producto.objects.all()
    historiaAll = Historial.objects.all()
    producto = Producto.objects.all()
    carritoall.delete()

    datos = {
        'listaCarrrito' : carritoall,
        'listaHistorial' : historiaAll
    }
        #plu_codigo = request.POST.get('codigo_producto')
       # productoA = Producto.objects.get(plu_codigo=plu_codigo)
    if request.method == 'POST':
        producto = Producto.objects.get(plu_codigo=request.POST.get('codigo_producto'))
        carrito = Carrito_Producto.objects.get(plu_codigo=producto)
        historial = Historial() 
        historial.plu_codigo = carrito
        historial.save()
               
    return render(request, 'app/pagar.html',datos)



        

@login_required
def historial(request):
    historialAll = Historial.objects.all()
    contador = Historial.objects.count()
    datos = {
        'listaHistorial' : historialAll,
        'contador' : contador
    }
    return render(request, 'app/historial.html', datos)



@login_required 
def suscripcion(request):
    return render(request,'app/suscripcion.html')

def seguimiento(request):
    return render(request,'app/seguimiento.html')

#plushtmls

@permission_required('app.add_producto') #LISTO
def agregar_producto(request):
    #return render(request,'app/agregar_producto.html')
    datos = {'form' : ProductoForm()}

    if request.method == 'POST' :
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto Agregado correctamente!')
            
    return render(request,'app/productos/agregar_producto.html',datos)

# SECCION MODIFICAR
@permission_required('app.change_producto') #listo
def modificar_producto(request, plu_codigo):
    producto = Producto.objects.get(plu_codigo=plu_codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES, instance=producto)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Producto modificado correctamente!')
            datos['form'] = formulario

    return render(request, 'app/productos/modificar_producto.html', datos)

@permission_required('app.view_producto') #listo
def listar_productos(request):
    datos = {'form' : ProductoForm()}
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
            
    return render(request,'app/productos/listar_productos.html',datos)

@permission_required('app.delete_producto') #LISTO
def eliminar_producto(request, plu_codigo):
    producto = Producto.objects.get(plu_codigo=plu_codigo)
    producto.delete()

    return redirect(to="listar_productos")

#crud usuarios

@permission_required('app.add_usuario') #LISTO

def agregar_usuario(request):
    datosu = {'formu' : UsuarioForm()}

    if request.method == 'POST' :
        formulario = UsuarioForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario guardado correctamente!')
            
    return render(request,'app/usuario/agregar_usuario.html',datosu)

@permission_required('app.change_usuario') #LISTO
def modificar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    datosu = {
        'formu' : UsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = UsuarioForm(data=request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario modificado correctamente!')
            datosu['formu'] = formulario

    return render(request, 'app/usuario/modificar_usuario.html', datosu)

@permission_required('app.view_usuario') #LISTO
def listar_usuarios(request):
    datosu = {'formu' : UsuarioForm()}
    UsuarioAll = Usuario.objects.all()
    datosu = {
        'listaUsuarios' : UsuarioAll
    }
            
    return render(request,'app/usuario/listar_usuarios.html',datosu)

@permission_required('app.delete_usuario') #LISTO
def eliminar_usuario(request, id_usuario):
    usuario = Usuario.objects.get(id_usuario=id_usuario)
    usuario.delete()

    return redirect(to="listar_usuarios")

def registro_usuario(request):
    datos = {
        'form' : RegistroUsuarioForm()
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            #user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            #login(request,user)
            messages.success(request,'Registrado correctamente!')
            #return redirect(to="home")
        datos["form"] = formulario

    return render(request, 'registration/registro_usuario.html', datos)

#registro de usuarios 

#def registro_usuarios(request):
    #datos = {
       # 'form' : RegistroUsuarioForm()
   # }    
    #if request.method == 'POST':
        #formulario = RegistroUsuarioForm(request.POST)
        #if formulario.is_valid():
           # formulario.save()
           # messages.success(request,'usuario registradocorrectamente!')
            
  #  return render(request,'registration/registro_usuario.html',datos)