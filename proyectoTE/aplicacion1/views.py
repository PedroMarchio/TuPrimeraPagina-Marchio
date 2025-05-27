from django.shortcuts import render
from django.http import HttpResponse
import datetime, random
from .models import *

# Create your views here.
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
    producto = productos(nombre=nombre, precio=precio, cantidad=cantidad)
    producto.save()
    return render(request, "aplicacion1/nueva_pagina.html", {"nombre":nombre, "precio":precio, "cantidad":cantidad,})
