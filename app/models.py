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
    nombre_producto = models.CharField(max_length=60)
    precio_producto = models.IntegerField()
    preciooferta = models.IntegerField(null=True)
    descripcion = models.CharField(max_length=100, null=False)
    imagen = models.ImageField(upload_to="carrito_producto", null=True)

    def __str__(self):
        return self.nombre_producto
    
    class Meta:
        db_table = 'db_carrito_producto'
    



class Carrito(models.Model):
     producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

     class Meta:
        db_table = 'db_carrito'
 








#pyton manage.py makemigrations -crea el script de la bd
#python manage.py migration -crea las tablas de la bd

#python manage.py createsuperuser - crea el usuario admin