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

    def __str__(self):
        return self.nombre
    

    class Meta:
        db_table = 'db_producto'
#pyton manage.py makemigrations -crea el script de la bd
#python manage.py migration -crea las tablas de la bd

#python manage.py createsuperuser - crea el usuario admin