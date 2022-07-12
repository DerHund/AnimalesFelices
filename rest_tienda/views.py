from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from Tienda.models import Productos,TipoProducto
from .serializers import ProductoSerializers , TipoProductoSerializers

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.
@csrf_exempt

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def ProductosApi(request):
    if request.method =='GET':
        Productos1 = Productos.objects.all()
        serializer = ProductoSerializers(Productos1,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        data1=JSONParser().parse(request)
        serializer = ProductoSerializers(data =data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def ProductosApi2(request):
    data1=JSONParser().parse(request)
    serializer = ProductoSerializers(data =data1)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlar_productos(request,idPro):
    try:
        producto = Productos.objects.get(idProducto=idPro)
    except Productos.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = ProductoSerializers(producto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = ProductoSerializers(producto,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        producto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
#############################

@api_view(['GET','POST'])
@permission_classes((IsAuthenticated,))
def TipoProductosApi(request):
    if request.method =='GET':
        Productos1 = TipoProducto.objects.all()
        serializer = TipoProductoSerializers(Productos1,many=True)
        return Response(serializer.data)
    elif request.method =='POST':
        data1=JSONParser().parse(request)
        serializer = TipoProductoSerializers(data =data1)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def TipoProductosApi2(request):
    data1=JSONParser().parse(request)
    serializer = TipoProductoSerializers(data =data1)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST) 

@api_view(['GET','PUT','DELETE'])
@permission_classes((IsAuthenticated,))
def controlar_Tipoproductos(request,idPro):
    try:
        tipoProducto = TipoProducto.objects.get(idTipoProducto=idPro)
    except TipoProducto.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    if request.method =='GET':
        serializer = TipoProductoSerializers(tipoProducto)
        return Response(serializer.data)
    elif request.method == 'PUT':
        data2 = JSONParser().parse(request)
        serializer = TipoProductoSerializers(tipoProducto,data = data2)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        TipoProducto.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
