from django import forms
from django.forms import ModelForm
from .models import Productos,Usuario

class ProductosForm(ModelForm):

    class Meta:
        model = Productos
        fields =['idProducto','nombreProducto','precioProducto','cantidadProducto','descripcionProducto','foto','tipoProducto']

class RegistroUsuarioForm(ModelForm):
    clave2 = forms.CharField(label='Repetir contraseña', max_length=100)
    class Meta:
        model = Usuario
        fields =['emailUsuario','claveUsuario']