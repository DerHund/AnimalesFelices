from django.contrib import admin
from django.urls import path 
from Tienda.views import Ofertas ,inicio,perros,gatos,Registro,Login,Articulo,EditarProducto,EliminarProducto,EditarPerfil,agregarProducto,Carrito

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/',inicio,name="index"),
    path('ofertas/',Ofertas,name="Ofertas"),
    path('perros/',perros,name="perros"),
    path('gatos/',gatos,name="gatos"),
    path('registro/',Registro,name="Registro"),
    path('login/',Login,name="Login"),
    path('articulo/',Articulo,name="Articulo"),
    path('editarProducto/',EditarProducto,name="EditarProducto"),
    path('eliminarProducto/',EliminarProducto,name="EliminarProducto"),
    path('editarPerfil/',EditarPerfil,name="EditarPerfil"),
    path('agregarProducto/',agregarProducto,name="agregarProducto"),
    path('carrito/',Carrito,name="Carrito"),
    
]
