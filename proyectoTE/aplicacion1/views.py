from django.shortcuts import render
from django.http import HttpResponse
import datetime, random
from .models import *
from .forms import *

# Create your views here. todo es practica que quedó jajjaa
def inicio(request):
    inicio = "Bien venidos a Django"
    return HttpResponse(inicio)

def bienvenida(request):
    hoy = datetime.datetime.now()
    saludo = f"""
    <html>
    <h1>Bienvenidos al curso de Django</h1>
    <h2>Hoy es {hoy}</h2>
    <h3>Gracias por venir maquina</h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido(request, nombre, apellido):
    hoy = datetime.datetime.now()
    saludo = f"""
    <html>
    <h1>Bienvenidos {nombre} {apellido} al curso de Django</h1>
    <h2>Hoy es {hoy}</h2>
    <h3>Gracias por venir maquina</h3>
    </html>
    """
    return HttpResponse(saludo)

def bienvenido_tpl(request):
    hoy = datetime.datetime.now()
    contexto = {"fecha": hoy, "nombre": "Pedro", "apellido": "Marchio"}
    return render(request, "aplicacion1/bienvenido.html", contexto)

def nueva_pagina(request):
    nombre = random.choices(["Pelota","Perro de Goma","Patito","Sapo","Tetera","Muñeca"], k=1)[0]
    precio = random.randint(100, 5001)
    cantidad = random.randint(100, 999)
    producto = Productos(nombre=nombre, precio=precio, cantidad=cantidad)
    producto.save()
    return render(request, "aplicacion1/nueva_pagina.html", {"nombre":nombre, "precio":precio, "cantidad":cantidad,})

#--------------------- desde acá hice el TP
def clientes_web(request):
    clientes = Clientes.objects.all()
    return render(request, "aplicacion1/clientes.html", {"clientes":clientes})

def clienteForm(request):
    if request.method == "POST":
        form = clientesForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            numeroContacto = form.cleaned_data["numeroContacto"]
            correo = form.cleaned_data["correo"]
            ciudad =form.cleaned_data["ciudad"]
            cliente = Clientes(nombre=nombre, apellido=apellido, numeroContacto=numeroContacto, correo=correo, ciudad=ciudad)
            cliente.save()
            clientes = Clientes.objects.all()
            return render(request, "aplicacion1/clientes.html", {"clientes": clientes})
    else:
        form = clientesForm()
    return render(request, "aplicacion1/cliente_form.html", {"form": form})

#---------------------
def productos_web(request):
    productos = Productos.objects.all()
    return render(request, "aplicacion1/productos.html", {"productos":productos})

def productoForm(request):
    if request.method == "POST":
        form = productosForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            precio = form.cleaned_data["precio"]
            cantidad = form.cleaned_data["cantidad"]
            producto = Productos(nombre=nombre, precio=precio, cantidad=cantidad)
            producto.save()
            productos = Productos.objects.all()
            return render(request, "aplicacion1/productos.html", {"productos": productos})
    else:
        form = productosForm()
    return render(request, "aplicacion1/producto_form.html", {"form": form})

#----------------------

def vendedores_web(request):
    vendedores = Vendedor.objects.all()
    return render(request, "aplicacion1/vendedores.html", {"vendedores":vendedores})

def vendedoresForm(request):
    if request.method == "POST":
        form = vendedorForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data["nombre"]
            apellido = form.cleaned_data["apellido"]
            numeroContacto = form.cleaned_data["numeroContacto"]
            correo = form.cleaned_data["correo"]
            ciudad =form.cleaned_data["ciudad"]
            vendedor = Vendedor(nombre=nombre, apellido=apellido, numeroContacto=numeroContacto, correo=correo, ciudad=ciudad)
            vendedor.save()
            vendedores = Vendedor.objects.all()
            return render(request, "aplicacion1/vendedores.html", {"vendedores": vendedores})
    else:
        form = vendedorForm()
    return render(request, "aplicacion1/vendedor_form.html", {"form": form})

