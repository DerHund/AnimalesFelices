from django.contrib import admin

from Tienda.views import carrito
from .models import  Productos,TipoProducto,TipoUsuario,Usuario,Carritos

# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(Productos)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)
admin.site.register(Carritos)