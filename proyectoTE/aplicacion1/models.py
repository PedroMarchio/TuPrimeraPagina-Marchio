from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    cantidad = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.cantidad}"

class Clientes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroContacto = models.IntegerField()
    correo = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Vendedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroContacto = models.IntegerField()
    correo = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class DueñosFerias(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    numeroContacto = models.IntegerField()
    correo = models.EmailField(max_length=50)
    ciudad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Ventas(models.Model):
    nombre = models.CharField(max_length=50)
    fecha_venta = models.DateField()
    cantidad = models.IntegerField()
    productoEntregado = models.BooleanField()
    productoCobrado = models.BooleanField()

    def __str__(self):
        return f"{self.fecha_venta}"
