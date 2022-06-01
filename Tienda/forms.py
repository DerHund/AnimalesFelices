from django import forms
from django.forms import ModelForm
from .models import Productos

class ProductosForm(ModelForm):

    class Meta:
        model = Productos
        fields =['idProducto','nombreProducto','precioProducto','cantidadProducto','descripcionProducto','foto','tipoProducto']

class ProductosFormEliminar(ModelForm):

    class Meta:
        model = Productos
        fields =['idProducto']