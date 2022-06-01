from django.contrib import admin
from django.urls import path 
from Tienda.views import  ListarProductos,ofertas,RecuperarContrasena  ,RecuperarContrasena, VistaAdministrador ,inicio,perros,gatos,Registro,Login,Articulo,EditarProducto,EliminarProducto,EditarPerfil,agregarProducto,Carrito
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="index"),
    path('ofertas/',ofertas,name="ofertas"),
    path('perros/',perros,name="perros"),
    path('gatos/',gatos,name="gatos"),
    path('registro/',Registro,name="registro"),
    path('login/',Login,name="login"),
    path('articulo/',Articulo,name="Articulo"),
    path('listarProductos/',ListarProductos,name="ListarProductos"),

    path('eliminarProducto/<id>',EliminarProducto,name="EliminarProducto"),
    path('editarProducto/<id>',EditarProducto,name="EditarProducto"),


    path('editarPerfil/',EditarPerfil,name="EditarPerfil"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('carrito/',Carrito,name="carrito"),
    path('VistaAdministrador/',VistaAdministrador,name="VistaAdministrador"),
    path('RecuperarContrasena/',RecuperarContrasena,name="RecuperarContrasena"),
    ]
urlpatterns += staticfiles_urlpatterns()


