from django.db import models

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

    def __int__(self):
        return self.plu_codigo
    

    class Meta:
        db_table = 'db_producto'

class Carrito_Producto(models.Model):
    plu_codigo = models.ForeignKey(Producto, on_delete=models.CASCADE)

    def __str__(self):
        return self.plu_codigo
    
    class Meta:
        db_table = 'db_carrito_producto'


class Usuario(models.Model):
    id_usuario = models.IntegerField(null=False,primary_key=True)
    usuario = models.CharField(max_length=20)
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.CharField(max_length=30)
    direccion = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=20)
    confirmar_contrasena = models.CharField(max_length=20)

    def __int__(self):
        return self.id_usuario
    
    class Meta:
        db_table = 'db_usuario'


class Suscriptor(models.Model):
    nombre_usuario = models.CharField(max_length=20,null=False, primary_key=True)
    suscrito = models.BooleanField(null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'db_suscriptor'

class Historial(models.Model):
    plu_codigo = models.ForeignKey(Carrito_Producto, on_delete=models.CASCADE)

    class Meta:
        db_table = "db_Historial"        





#pyton manage.py makemigrations -crea el script de la bd
#python manage.py migration -crea las tablas de la bd

#python manage.py createsuperuser - crea el usuario admin