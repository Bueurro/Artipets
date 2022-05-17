from django.urls import path
from .views import *

urlpatterns = [
    path('',index, name="index"),
    path('login',login, name="login"),
    path('home',homelogin, name="homelogin"),
    path('bandanas',bandanas, name="bandanas"),
    path('bandanasnl',bandanasnl, name="bandanasnl"),
    path('comidas',comidas, name="comidas"),
    path('comidasnl',comidasnl, name="comidasnl"),
    path('correas',correas, name="correas"),
    path('correasnl',correasnl, name="correasnl"),
    path('identificaciones',identificaciones, name="identificaciones"),
    path('identificacionesnl',identificacionesnl, name="identificacionesnl"),
    path('carrito',carrito, name="carrito"),
    path('historial',historial, name="historial"),
    path('suscripcion',suscripcion, name="suscripcion"),
    path('agregar_producto',agregar_producto, name="agregar_producto"),
    path('modificar_producto/<plu_codigo>/',modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<plu_codigo>/',eliminar_producto, name="eliminar_producto"),
    path('listar_productos',listar_productos, name="listar_productos"),
    path('agregar_usuario',agregar_usuario, name="agregar_usuario"),
    path('modificar_usuario/<id_usuario>/',modificar_usuario, name="modificar_usuario"),
    path('eliminar_usuario/<id_usuario>/',eliminar_usuario, name="eliminar_usuario"),
    path('listar_usuarios',listar_usuarios, name="listar_usuarios"),
    path('pagar',pagar, name="pagar"),
]