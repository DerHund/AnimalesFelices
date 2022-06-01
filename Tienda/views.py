from django.shortcuts import render ,redirect
from .models import Productos
from django.db.models import Q
from .forms import ProductosForm

# Create your views here.
def inicio (request):
    return render(request, 'Tienda/index.html')

def agregarProducto (request):
    datos = {
        'form' : ProductosForm()
    }

    if request.method =='POST':
        formulario = ProductosForm(request.POST,request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado con exito"
        else:
            datos['mensaje'] = "Error al guardar"

    return render(request, 'Tienda/agregarProducto.html' ,datos)

def Articulo (request):
    return render(request, 'Tienda/Articulo.html')

def Carrito (request):
    return render(request , 'Tienda/Carrito.html')

def EditarPerfil (request):
    return render(request, 'Tienda/EditarPerfil.html')

def EditarProducto (request , id):
    producto = Productos.objects.get(idProducto=id)
    datos={
        'form': ProductosForm(instance=producto)
    }
    if request.method =='POST':
        formulario =ProductosForm(data=request.POST ,instance=producto)##Error al guardar imagenes nuevas
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Guardado con exito"
        else:
            datos['mensaje'] = "Error al guardar" 

    return render(request, 'Tienda/EditarProducto.html',datos)


def EliminarProducto (request,id):
    producto = Productos.objects.get(idProducto=id)
    datos={
        'form': ProductosForm(instance=producto)
    }
    if request.method =='POST':
        formulario =ProductosForm(data=request.POST ,instance=producto)##Error al guardar imagenes nuevas
        if formulario.is_valid():
            producto.delete()
            datos['mensaje'] = "Eliminado con exito"
        else:
            datos['mensaje'] = "Error al Eliminar" 

    return render(request , 'Tienda/EliminarProducto.html',datos)



def gatos (request):
    productos = Productos.objects.filter(tipoProducto=1).filter(~Q(cantidadProducto=0))

    datos = {
        'productos': productos
    }

    return render(request, 'Tienda/gatos.html' , datos)

def Login (request):
    return render(request, 'Tienda/Login.html')

def ofertas (request):
    productos = Productos.objects.filter(tipoProducto=3).filter(~Q(cantidadProducto=0))

    datos = {
        'productos': productos
    }
    return render(request, 'Tienda/Ofertas.html',datos)

def perros (request):
    productos = Productos.objects.filter(tipoProducto=2).filter(~Q(cantidadProducto=0))

    datos = {
        'productos': productos
    }
    return render(request, 'Tienda/perros.html',datos)

def RecuperarContrasena (request):
    return render(request, 'Tienda/RecuperarContrasena.html')

def Registro (request):
    return render(request, 'Tienda/Registro.html')

def VistaAdministrador (request):
    return render(request, 'Tienda/VistaAdministrador.html')

def ListarProductos(request):
    productos=Productos.objects.all()
    datos={
        'productos':productos
    }
    return render(request ,'Tienda/ListarProductos.html',datos)