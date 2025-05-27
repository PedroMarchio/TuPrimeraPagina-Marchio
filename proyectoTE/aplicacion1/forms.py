from django import forms

class productosForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    precio = forms.IntegerField(required=True)
    cantidad = forms.IntegerField(required=True)


class clientesForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    numeroContacto = forms.IntegerField(required=True)
    correo = forms.EmailField(max_length=50, required=True)
    ciudad = forms.CharField(max_length=50)


class vendedorForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    numeroContacto = forms.IntegerField(required=True)
    correo = forms.EmailField(max_length=50, required=True)
    ciudad = forms.CharField(max_length=50)


class dueñosFeriasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    apellido = forms.CharField(max_length=50, required=True)
    numeroContacto = forms.IntegerField(required=True)
    correo = forms.EmailField(max_length=50, required=True)
    ciudad = forms.CharField(max_length=50)


class ventasForm(forms.Form):
    nombre = forms.CharField(max_length=50, required=True)
    fecha_venta = forms.DateField(required=True)
    cantidad = forms.IntegerField(required=True)
    productoEntregado = forms.BooleanField(required=True)
    productoCobrado = forms.BooleanField(required=True)

