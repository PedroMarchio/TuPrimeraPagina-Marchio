from django.db import models

# Create your models here.
class productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

class clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroContacto = models.IntegerField()
    correo = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=50)

class vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroContacto = models.IntegerField()
    correo = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=50)

class dueñosFerias(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroContacto = models.IntegerField()
    correo = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=50)

class ventas(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_venta = models.DateField()
    cantidad = models.IntegerField()
    productoEntregado = models.BooleanField()
    productoCobrado = models.BooleanField()
