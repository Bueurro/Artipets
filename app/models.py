from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo

    class Meta:
        db_table = 'db_tipo_producto'
#una funcion para hacer un To_String       
#al migrar se colocan las claves 

class Producto(models.Model):
    plu_codigo = models.IntegerField(null=False,primary_key=True)
    stock = models.IntegerField()
    precio = models.IntegerField()
    preciooferta = models.IntegerField()
    nombre = models.CharField(max_length=60)
    marca = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=80)
    #hacer la union con la clave foranea 
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.nombre
    


    class Meta:
        db_table = 'db_producto'

class Carrito_Producto(models.Model):
    car_codigo = models.AutoField(primary_key=True)
    imagen_car = models.ImageField(upload_to="carrito", null = True)
    nombre_car = models.CharField(max_length=60)
    precio_car = models.IntegerField()
    preciooferta_car = models.IntegerField()
    descripcion_car = models.CharField(max_length=80)
    cantidad = models.IntegerField()
    totales =  models.IntegerField(blank=True)
    usuario_car = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre_car
    
    class Meta:
        db_table = 'db_carrito'

class Usuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    suscripcion = models.BooleanField()

    def __str__(self):
        return str(self.usuario.username)
    
    class Meta:
        db_table = 'db_usuario'


class Suscriptor(models.Model):
    nombre_usuario = models.CharField(max_length=20,null=False, primary_key=True)
    suscrito = models.BooleanField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'db_suscriptor'

class Pedido(models.Model):
    codigo = models.AutoField(primary_key=True)
    productos = models.CharField(max_length=250)
    cantidad = models.IntegerField()
    total = models.IntegerField()
    fecha = models.DateField()
    estado = models.CharField(max_length=20)
    cliente = models.CharField(max_length=20)

    def __str__(self):
        return str(self.codigo)
    
    class Meta:
        db_table = 'db_pedido'

class Estado_Pedido(models.Model):
    estado = models.CharField(max_length=20)

    def __str__(self):
        return str(self.estado)
    
    class Meta:
        db_table = 'db_estado_pedido'

#pyton manage.py makemigrations -crea el script de la bd
#python manage.py migration -crea las tablas de la bd

#python manage.py createsuperuser - crea el usuario admin