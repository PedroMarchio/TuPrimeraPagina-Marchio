from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.bienvenido_tpl, name="inicio"),
    #path('bienvenida/', views.bienvenida, name="bienvenida"),
    #path('bienvenido/<nombre>/<apellido>/', views.bienvenido, name="bienvenido"),
    #path('bienvenido_tpl/', views.bienvenido_tpl, name="bienvenido_tpl"),
    #path('nueva_pagina/', views.nueva_pagina, name="nueva_pagina"),
    path('clientes/', views.clientes_web, name="clientes"),
    path('clientes_form/', views.clienteForm, name="clientes_form"),
    path('productos/', views.productos_web, name="productos"),
    path('productos_form/', views.productoForm, name="productos_form"),
    path('vendedores/', views.vendedores_web, name="vendedores"),
    path('vendedor_form/', views.vendedoresForm, name="vendedor_form"),
]