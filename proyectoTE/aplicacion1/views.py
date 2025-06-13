from django.shortcuts import render
from .models import *
from .forms import *
from django.shortcuts import redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

def inicio(request):
    productos = Productos.objects.all()
    return render(request, 'aplicacion1/inicio.html', {'productos': productos})

#---------------CBV------------------
class StaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('inicio') 

class ProductosList(StaffRequiredMixin, ListView):
    model = Productos

class ProductosCreate(StaffRequiredMixin, CreateView):
    model = Productos
    fields = ["nombre", "precio", "cantidad", "imagen"]
    success_url = reverse_lazy("productos")

class ProductosUpdate(StaffRequiredMixin, UpdateView):
    model = Productos
    fields = ["nombre", "precio", "cantidad", "imagen"]
    success_url = reverse_lazy("productos")

class ProductosDelete(StaffRequiredMixin, DeleteView):
    model = Productos
    fields = ["nombre", "precio", "cantidad"]
    success_url = reverse_lazy("productos")

class VendedorList(StaffRequiredMixin, ListView):
    model = Vendedor

class VendedorCreate(StaffRequiredMixin, CreateView):
    model = Vendedor
    fields = ["nombre", "apellido", "numeroContacto", "correo", "ciudad"]
    success_url = reverse_lazy("vendedores")

class VendedorUpdate(StaffRequiredMixin, UpdateView):
    model =  Vendedor
    fields = ["nombre", "apellido", "numeroContacto", "correo", "ciudad"]
    success_url = reverse_lazy("vendedores")

class VendedorDelete(StaffRequiredMixin, DeleteView):
    model =  Vendedor
    fields = ["nombre", "apellido", "numeroContacto", "correo", "ciudad"]
    success_url = reverse_lazy("vendedores")

class ClientesList(StaffRequiredMixin, ListView):
    model = Clientes

class ClientesCreate(StaffRequiredMixin, CreateView):
    model = Clientes
    fields = ["nombre", "apellido", "numeroContacto", "correo", "ciudad"]
    success_url = reverse_lazy("clientes")

class ClientesUpdate(StaffRequiredMixin, UpdateView):
    model = Clientes
    fields = ["nombre", "apellido", "numeroContacto", "correo", "ciudad"]
    success_url = reverse_lazy("clientes")

class ClientesDelete(StaffRequiredMixin, DeleteView):
    model = Clientes
    fields = ["nombre", "apellido", "numeroContacto", "correo", "ciudad"]
    success_url = reverse_lazy("clientes")

def register(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.success(request, "Usuario creado exitosamente.")
            return redirect('inicio')
    else:
        form = RegistroForm()

    return render(request, 'aplicacion1/registro.html', {'form': form})

def loginRequest(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            return redirect('inicio')
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
            return redirect('login')
    return render(request, 'aplicacion1/login.html')

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.first_name = miForm.cleaned_data.get("first_name")
            user.last_name = miForm.cleaned_data.get("last_name")
            user.save()
            return redirect(reverse_lazy("inicio"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "aplicacion1/editarPerfil.html", {"form": miForm})

class CambiarClave(LoginRequiredMixin, PasswordChangeView):
    template_name = "aplicacion1/cambiar_clave.html"
    success_url = reverse_lazy("inicio")

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            imagen = miForm.cleaned_data["imagen"]
            #_________ Borrar avatares viejos
            avatarViejo = Avatar.objects.filter(user=usuario)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()
            #__________________________________________
            avatar = Avatar(user=usuario, imagen=imagen)
            avatar.save()

            #_________ Enviar la imagen al home
            imagen = Avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            #____________________________________________________
            return redirect(reverse_lazy("inicio"))
    else:
        miForm = AvatarForm()
    return render(request, "aplicacion1/agregarAvatar.html", {"form": miForm})

def sobreMi(request):
    return render(request, "aplicacion1/about.html")