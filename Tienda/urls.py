from Tienda.forms import RegistroUsuarioForm
from . import views
from django.contrib import admin
from django.urls import path ,include
from Tienda.views import  carrito,ListarProductos,ofertas ,inicio,perros,gatos,Articulo,EditarProducto,EliminarProducto,EditarPerfil,agregarProducto
from .views import  VaciarCarrito, agregarAlCarrito , SignUpView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="index"),
    path('ofertas/',ofertas,name="ofertas"),
    path('perros/',perros,name="perros"),
    path('gatos/',gatos,name="gatos"),

    path('articulo/<id>',Articulo,name="Articulo"),

    path('listarProductos/',ListarProductos,name="ListarProductos"),
    path('eliminarProducto/<id>',EliminarProducto,name="EliminarProducto"),
    path('editarProducto/<id>',EditarProducto,name="EditarProducto"),

    path("accounts/", include("django.contrib.auth.urls")), 
    path("registro/", SignUpView.as_view(), name="registro"),


    path('editarPerfil/',EditarPerfil,name="EditarPerfil"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),


    path('carrito/',carrito,name="carrito"),
    path('agregarAlCarrito/<id>' ,agregarAlCarrito , name = 'agregarAlCarrito'),
    path('VaciarCarrito/',VaciarCarrito,name="VaciarCarrito"),

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



