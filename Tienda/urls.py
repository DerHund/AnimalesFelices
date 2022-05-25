from django.contrib import admin
from django.urls import path 
from Tienda.views import ofertas,RecuperarContrasena  ,RecuperarContrasena, VistaAdministrador ,inicio,perros,gatos,Registro,Login,Articulo,EditarProducto,EliminarProducto,EditarPerfil,agregarProducto,Carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="index"),
    path('ofertas/',ofertas,name="ofertas"),
    path('perros/',perros,name="perros"),
    path('gatos/',gatos,name="gatos"),
    path('registro/',Registro,name="registro"),
    path('login/',Login,name="login"),
    path('articulo/',Articulo,name="Articulo"),
    path('editarProducto/',EditarProducto,name="EditarProducto"),
    path('eliminarProducto/',EliminarProducto,name="EliminarProducto"),
    path('editarPerfil/',EditarPerfil,name="EditarPerfil"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('carrito/',Carrito,name="carrito"),
    path('VistaAdministrador/',VistaAdministrador,name="VistaAdministrador"),
    path('RecuperarContrasena/',RecuperarContrasena,name="RecuperarContrasena"),
]
