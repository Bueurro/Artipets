from calendar import c
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from app.forms import ProductoForm
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login
import requests
from itertools import count
#---------------------


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
        productostock = Producto.objects.get(plu_codigo=plu_codigo)
        productostock.stock -= 1
        productostock.save()
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
        productostock = Producto.objects.get(plu_codigo=plu_codigo)
        productostock.stock -= 1
        productostock.save()
        messages.success(request,'Producto Enviado al carrito correctamente!')
        
    return render(request, 'app/comidas.html', datos)

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
        productostock = Producto.objects.get(plu_codigo=plu_codigo)
        productostock.stock -= 1
        productostock.save()
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
        productostock = Producto.objects.get(plu_codigo=plu_codigo)
        productostock.stock -= 1
        productostock.save()
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
    carrito = Carrito_Producto.objects.all()
    contador = Carrito_Producto.objects.count()
       
    datos = { 'listacarrrito' : carrito,
              'contador' : contador,
                 
    
    # hacer un if para mostrar el permiso de si esta suscrtito para mostrar el total con descuento o el total normalito 
    'Total': round(sum(v.plu_codigo.precio for v in carrito)),
    'descuento_suscriptor': round(sum(v.plu_codigo.precio*0.05 for v in carrito)),
    'TotalPagar': round(sum(v.plu_codigo.precio - v.plu_codigo.precio*0.05 for v in carrito)),
    
    }

    return render(request, 'app/carrito.html',datos)

@permission_required('app.view_carrito_producto')
def eliminar_carrito(request, id):
    productocarro = Carrito_Producto.objects.get(id=id)
    productocarro.delete()
   

    

    

    return redirect(to="carrito")


@login_required 
def pagar(request):
    carrito = Carrito_Producto.objects.all()
    historia = Historial.objects.all()
    producto = Producto.objects.all()
    carrito.delete()

    datos = {
        'listacarrrito' : carrito,
        'listaHistorial' : historia,
    }
        #plu_codigo = request.POST.get('codigo_producto')
       # productoA = Producto.objects.get(plu_codigo=plu_codigo)
    if request.method == 'POST':
        producto = Producto.objects.get(plu_codigo=request.POST.get('codigo_producto'))
        carrito = Carrito_Producto.objects.get(plu_codigo=producto)
        historial = Historial() 
        historial.plu_codigo = carrito
        historial.save()
        historial.save()
        
    return render(request, 'app/pagar.html',datos)



        

@login_required
def historial(request):
    historial = Historial.objects.all()
    contador = Historial.objects.count()

    datos = {
        'listaHistorial' : historial,
        'contador' : contador
    }
    redirect  (to ='historial')
    return render(request, 'app/historial.html', datos)



@login_required 
def suscripcion(request):
    return render(request,'app/suscripcion.html')

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
    productos = Producto.objects.all()
    datos = {
        'listaProductos' : productos,
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

@login_required 
def api_digimon(request):
    response = requests.get('https://digimon-api.vercel.app/api/digimon').json()

    datos = {
        'listaDigimon' : response,
    }
    return render(request, 'app/api_digimon.html', datos)

def listaapi(request):
    response = requests.get('http://127.0.0.1:8000/api/producto/').json()

    datos = { 
        'ListaApi' : response
        }

    return render(request,'app/listas/listaapi.html',datos)

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