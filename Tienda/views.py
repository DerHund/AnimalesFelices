from datetime import timezone
from django.shortcuts import render ,redirect
from .models import Carritos, Productos
from django.db.models import Q
from .forms import ProductosForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

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

def Articulo (request,id):
    producto = Productos.objects.get(idProducto=id)
    datos = {
        'productos': producto
    }

    return render(request, 'Tienda/Articulo.html',datos)


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




def VistaAdministrador (request):
    return render(request, 'Tienda/VistaAdministrador.html')

def ListarProductos(request):
    productos=Productos.objects.all()
    datos={
        'productos':productos
    }
    return render(request ,'Tienda/ListarProductos.html',datos)

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/registro.html"

def agregarAlCarrito(request , id):
    productos=Productos.objects.get(idProducto=id)
    p=Carritos(producto=productos,cantidad=1)
    p.save()
    return redirect('carrito')

def carrito(request):
    objetos=Carritos.objects.all()
    datos={
        'objetos':objetos
    }
    return render(request, 'Tienda/carrito.html',datos)

def VaciarCarrito(request):
    productos=Carritos.objects.all()
    productos.delete()
    return redirect('index')

 