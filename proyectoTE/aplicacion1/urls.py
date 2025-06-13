from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="inicio"),

    path('productos/', views.ProductosList.as_view(), name="productos"),
    path('productosCreate/', views.ProductosCreate.as_view(), name="productosCreate"),
    path('productosUpdate/<int:pk>', views.ProductosUpdate.as_view(), name="productosUpdate"),
    path('productosDelete/<int:pk>', views.ProductosDelete.as_view(), name="productosDelete"),

    path('vendedores/', views.VendedorList.as_view(), name="vendedores"),
    path('vendedoresCreate/', views.VendedorCreate.as_view(), name="vendedoresCreate"),
    path('vendedoresUpdate/<int:pk>', views.VendedorUpdate.as_view(), name="vendedoresUpdate"),
    path('vendedoresDelete/<int:pk>', views.VendedorDelete.as_view(), name="vendedoresDelete"),

    path('clientes/', views.ClientesList.as_view(), name="clientes"),
    path('clientesCreate/', views.ClientesCreate.as_view(), name="clientesCreate"),
    path('clientesUpdate/<int:pk>', views.ClientesUpdate.as_view(), name="clientesUpdate"),
    path('clientesDelete/<int:pk>', views.ClientesDelete.as_view(), name="clientesDelete"),

    path('registro/', views.register, name="registro"),
    path('login/', views.loginRequest, name="login"),
    path('logout/', LogoutView.as_view(next_page='inicio'), name='logout'),
    path('editarPerfil/', views.editarPerfil, name='editarPerfil'),
    path('password/', views.CambiarClave.as_view(), name='cambiar_clave'),
    path('agregar_avatar/', views.agregarAvatar, name="agregar_avatar"),

    path('about/', views.sobreMi, name="about"),
    
]