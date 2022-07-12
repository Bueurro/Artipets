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
from datetime import date
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
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
        pcodigo = request.POST.get('car_codigo')
        producto = Producto.objects.get(plu_codigo=pcodigo)

        tipoProducto = TipoProducto()
        tipoProducto.tipo = request.POST.get('tipo')
        productostock = Producto.objects.get(plu_codigo=pcodigo)

        if producto.stock > 0:
            productostock.stock -= 1
            productostock.save()
            
            codigop = request.POST.get('car_codigo')
            cantidadprod = Carrito_Producto.objects.filter(car_codigo=codigop)
            
            if cantidadprod:
                cont = Carrito_Producto.objects.get(car_codigo=pcodigo)
                cont.cantidad += 1
                cont.save()

            else:
                cont = Carrito_Producto()
                cont.car_codigo = request.POST.get('car_codigo')
                cont.imagen_car = request.POST.get('imagen_car')
                cont.nombre_car = request.POST.get('nombre_car')
                cont.precio_car = request.POST.get('precio_car')
                cont.preciooferta_car = request.POST.get('preciooferta_car')
                cont.descripcion_car = request.POST.get('descripcion_car')
                cont.cantidad = 1
                cont.totales = 0
                cont.usuario_car = request.user.username
                cont.save()

            messages.success(request,'Producto Enviado al carrito correctamente!')
        else:
            messages.success(request, 'No hay existencias para agregar al carrito')
    
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
        pcodigo = request.POST.get('car_codigo')
        producto = Producto.objects.get(plu_codigo=pcodigo)

        tipoProducto = TipoProducto()
        tipoProducto.tipo = request.POST.get('tipo')
        productostock = Producto.objects.get(plu_codigo=pcodigo)

        if producto.stock > 0:
            productostock.stock -= 1
            productostock.save()
            
            codigop = request.POST.get('car_codigo')
            cantidadprod = Carrito_Producto.objects.filter(car_codigo=codigop)
            
            if cantidadprod:
                cont = Carrito_Producto.objects.get(car_codigo=pcodigo)
                cont.cantidad += 1
                cont.save()

            else:
                cont = Carrito_Producto()
                cont.car_codigo = request.POST.get('car_codigo')
                cont.imagen_car = request.POST.get('imagen_car')
                cont.nombre_car = request.POST.get('nombre_car')
                cont.precio_car = request.POST.get('precio_car')
                cont.preciooferta_car = request.POST.get('preciooferta_car')
                cont.descripcion_car = request.POST.get('descripcion_car')
                cont.cantidad = 1
                cont.totales = 0
                cont.usuario_car = request.user.username
                cont.save()

            messages.success(request,'Producto Enviado al carrito correctamente!')
        else:
            messages.success(request, 'No hay existencias para agregar al carrito')
        
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
        pcodigo = request.POST.get('car_codigo')
        producto = Producto.objects.get(plu_codigo=pcodigo)

        tipoProducto = TipoProducto()
        tipoProducto.tipo = request.POST.get('tipo')
        productostock = Producto.objects.get(plu_codigo=pcodigo)

        if producto.stock > 0:
            productostock.stock -= 1
            productostock.save()
            
            codigop = request.POST.get('car_codigo')
            cantidadprod = Carrito_Producto.objects.filter(car_codigo=codigop)
            
            if cantidadprod:
                cont = Carrito_Producto.objects.get(car_codigo=pcodigo)
                cont.cantidad += 1
                cont.save()

            else:
                cont = Carrito_Producto()
                cont.car_codigo = request.POST.get('car_codigo')
                cont.imagen_car = request.POST.get('imagen_car')
                cont.nombre_car = request.POST.get('nombre_car')
                cont.precio_car = request.POST.get('precio_car')
                cont.preciooferta_car = request.POST.get('preciooferta_car')
                cont.descripcion_car = request.POST.get('descripcion_car')
                cont.cantidad = 1
                cont.totales = 0
                cont.usuario_car = request.user.username
                cont.save()

            messages.success(request,'Producto Enviado al carrito correctamente!')
        else:
            messages.success(request, 'No hay existencias para agregar al carrito')

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
        pcodigo = request.POST.get('car_codigo')
        producto = Producto.objects.get(plu_codigo=pcodigo)

        tipoProducto = TipoProducto()
        tipoProducto.tipo = request.POST.get('tipo')
        productostock = Producto.objects.get(plu_codigo=pcodigo)

        if producto.stock > 0:
            productostock.stock -= 1
            productostock.save()
            
            codigop = request.POST.get('car_codigo')
            cantidadprod = Carrito_Producto.objects.filter(car_codigo=codigop)
            
            if cantidadprod:
                cont = Carrito_Producto.objects.get(car_codigo=pcodigo)
                cont.cantidad += 1
                cont.save()

            else:
                cont = Carrito_Producto()
                cont.car_codigo = request.POST.get('car_codigo')
                cont.imagen_car = request.POST.get('imagen_car')
                cont.nombre_car = request.POST.get('nombre_car')
                cont.precio_car = request.POST.get('precio_car')
                cont.preciooferta_car = request.POST.get('preciooferta_car')
                cont.descripcion_car = request.POST.get('descripcion_car')
                cont.cantidad = 1
                cont.totales = 0
                cont.usuario_car = request.user.username
                cont.save()

            messages.success(request,'Producto Enviado al carrito correctamente!')
        else:
            messages.success(request, 'No hay existencias para agregar al carrito')

    return render(request,'app/identificaciones.html',datos)

def identificacionesnl(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request,'app/identificacionesnl.html',datos)

#logOptions

@login_required #LISTO
def carrito(request):
    productosAll = Producto.objects.all()
    propietario = request.user.username
    carritoAll = Carrito_Producto.objects.filter(usuario_car = propietario)
    contador = 0


    for producto in carritoAll:
        producto.totales = producto.precio_car * producto.cantidad
        producto.save()
        contador = contador + producto.totales

    usuarioq = request.user
    userx = Usuario.objects.get(usuario = usuarioq)

    if userx.suscripcion == True:
        total = round(contador - ( contador * 0.05))
    else:
        total = round(contador)

    datos = {
        'listacarrrito' : carritoAll,
        'contador' : contador,
        'Total': total,
        'Carrovacio' : productosAll,
    }

    return render(request, 'app/carrito.html',datos)


@login_required
def eliminar_carrito(request, car_codigo):

    productocarro = Carrito_Producto.objects.get(car_codigo=car_codigo)
    productos = Producto.objects.get(plu_codigo=car_codigo)

    if productocarro.cantidad > 1:
        productocarro.cantidad -= 1 
        productocarro.save()
        productos.stock += 1
        productos.save()
    else:
        productocarro.delete()
        productos.stock += 1
        productos.save()

    return redirect(to="carrito")


@login_required
def pagar(request):
    usuarioq = request.user.username
    CarritoAll = Carrito_Producto.objects.filter(usuario_car = usuarioq)

    productosl = " "
    for producto in CarritoAll:
        productosl = "" + productosl + producto.nombre_car + " [ " + str(producto.cantidad) + " ] | "

    fecha = date.today()
    cantidad_productos = len(CarritoAll)

    total = 0
    for producto in CarritoAll:
        total = total + producto.totales

    cliente = request.user.username 


    pedido = Pedido()
    pedido.productos = productosl
    pedido.cantidad = cantidad_productos
    pedido.total = total
    pedido.fecha = fecha
    pedido.estado = 'En Preparación'
    pedido.cliente = cliente
    pedido.save()
    CarritoAll.delete()
        
    return render(request, 'app/pagar.html')


@login_required
def historial(request):
    
    usuarioq = request.user.username
    historial = Pedido.objects.filter(cliente=usuarioq)
    

    datos = {
        'listaHistorial' : historial,
    }

    return render(request, 'app/historial.html', datos)

@permission_required('app.change_estado_pedido') #listo
def historial_general(request):

    historial = Pedido.objects.all()

    datos = {
        'listaHistorial' : historial,
    }

    return render(request, 'app/historial_general.html', datos)



@login_required 
def suscripcion(request):

    if request.POST:
        uservalid = request.user.username
        susex = Suscriptor.objects.filter(nombre_usuario=uservalid)
        data = Suscriptor(nombre_usuario=uservalid)
        validsus = data.suscrito

        if susex:
            if validsus == 1:
                messages.success(request, "Usted ya está suscrito")
            else:
                susnueva = Suscriptor()
                susnueva.nombre_usuario = uservalid
                susnueva.suscrito = True
                susnueva.save()
                messages.success(request, "Suscripción exitosa.")
        else:
            susnueva = Suscriptor()
            susnueva.nombre_usuario = uservalid
            susnueva.suscrito = True
            susnueva.save()
            messages.success(request, "Suscripción exitosa.")
            

    if request.GET:
        uservalid = request.user.username
        susex = Suscriptor.objects.filter(nombre_usuario=uservalid)
        data = Suscriptor(nombre_usuario=uservalid)
        validsus = data.suscrito

        if susex:
            if validsus == 0:
                messages.success(request, "Usted no está suscrito.")
            else:
                susnueva = Suscriptor()
                susnueva.nombre_usuario = uservalid
                susnueva.suscrito = False
                susnueva.save()
            messages.success(request, "Usted ya no está suscrito")
        else:
            susnueva = Suscriptor()
            susnueva.nombre_usuario = uservalid
            susnueva.suscrito = False
            susnueva.save()


    return render(request,'app/suscripcion.html')

#plushtmls

def modificar_estado(request, codigo):
    codigoq = codigo
    pedido = Pedido.objects.get(codigo=codigoq)

    datos = {
        'form' : PedidoForm(instance=pedido)
    }

    if request.method == 'POST':
        formulario = PedidoForm(data=request.POST, instance=pedido)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Estado modificado correctamente.')
            datos['form'] = formulario

    return render(request, 'app/modificar_estado.html', datos)


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

@permission_required('app.change_usuario') 
def modificar_usuario(request, id):
    usuario =  User.objects.get(id=id)
    datos = {
        'form' : RegistroUsuarioForm(instance=usuario)
    }
    if request.method == 'POST':
        formulario = RegistroUsuarioForm(request.POST, files=request.FILES, instance=usuario)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,'Usuario modificado correctamente!')
            datos['form'] = formulario
    return render(request,'app/usuario/modificar_usuario.html', datos) 


@permission_required('app.view_usuario')
def listar_usuarios(request):
    usuarios = User.objects.all()
    datosu = {
        'listaUsuarios' : usuarios
    }
    return render(request,'app/usuario/listar_usuarios.html',datosu)

@permission_required('app.delete_usuario')
def eliminar_usuario(request, id):
    usuario = User.objects.get(id=id)
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
            user  = formulario.save()
            group = Group.objects.get(name='cliente')
            group.user_set.add(user)
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

@login_required
def seguimiento(request, codigo):

    ordenq = codigo
    historial = Pedido.objects.filter(codigo=ordenq)
    

    datos = {
        'listaHistorial' : historial,
    }

    return render(request, 'app/seguimiento.html',datos)


#final