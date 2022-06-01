from django import forms
from django.forms import ModelForm
from .models import Productos,Usuario

class ProductosForm(ModelForm):

    class Meta:
        model = Productos
        fields =['idProducto','nombreProducto','precioProducto','cantidadProducto','descripcionProducto','foto','tipoProducto']

class RegistroUsuarioForm(ModelForm):

    class Meta:
        model = Usuario
        fields =['idUsuario','nombreUsuario','apellidoUsuario','claveUsuario','emailUsuario','telefonoUsuario','direccionUsuario','regionUsuario','comunaUsuario','codigoPostalUsuario','tipoUsuario']