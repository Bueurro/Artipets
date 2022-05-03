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
]