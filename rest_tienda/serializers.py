from rest_framework import serializers
from Tienda.models import Productos , TipoProducto

class ProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields =['idProducto','nombreProducto','precioProducto','cantidadProducto','descripcionProducto','foto','tipoProducto']
class TipoProductoSerializers(serializers.ModelSerializer):
    class Meta:
        model = TipoProducto
        fields =['idTipoProducto','nombreTipo']