from django.urls import path
from rest_tienda.views import controlar_Tipoproductos , controlar_productos , TipoProductosApi2 , TipoProductosApi , ProductosApi2 , ProductosApi
from rest_tienda.viewsLogin import login




urlpatterns = [
    path('login/',login,name="login"),

    path('ProductosApi/',ProductosApi,name="ProductosApi"),
    path('ProductosApi2/',ProductosApi2,name="ProductosApi2"),

    path('TipoProductosApi/',TipoProductosApi,name="TipoProductosApi"),
    path('TipoProductosApi2/',TipoProductosApi2,name="TipoProductosApi2"),


    path('controlar_productos/<idPro>',controlar_productos,name="controlar_productos"),
    path('controlar_Tipoproductos/<idPro>',controlar_Tipoproductos,name="controlar_Tipoproductos"),
]