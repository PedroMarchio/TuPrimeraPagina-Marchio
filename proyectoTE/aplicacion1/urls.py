from django.urls import path
from . import views

urlpatterns = [
    path('inicio/', views.inicio, name="inicio"),
    path('bienvenida/', views.bienvenida, name="bienvenida"),
    path('bienvenido/<nombre>/<apellido>/', views.bienvenido, name="bienvenido"),
    path('bienvenido_tpl/', views.bienvenido_tpl, name="bienvenido_tpl"),
    path('nueva_pagina/', views.nueva_pagina, name="nueva_pagina"),
    path('clientes/', views.clientes_web, name="clientes"),
]