from django.db import models

# Create your models here.

class TipoProducto(models.Model):
    tipo = models.CharField(max_length=20)

    def __str__(self):
        return self.tipo
#una funcion para hacer un To_String       
#al migrar se colocan las claves 

class Producto(models.Model):
    plu_codigo = models.IntegerField()
    stock = models.IntegerField()
    precio = models.IntegerField()
    nombre = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=40)
    #hacer la union con la clave foranea 
    tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to="productos", null=True)
    fecha_ingreso = models.DateField()

    def __str__(self):
        return self.nombre
    
#pyton manage.py makemigrations -crea el script de la bd
#python manage.py migration -crea las tablas de la bd

#python manage.py createsuperuser - crea el usuario admin