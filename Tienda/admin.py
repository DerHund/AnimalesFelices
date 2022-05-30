from django.contrib import admin
from .models import Productos,TipoProducto,TipoUsuario,Usuario

# Register your models here.
admin.site.register(TipoProducto)
admin.site.register(Productos)
admin.site.register(TipoUsuario)
admin.site.register(Usuario)