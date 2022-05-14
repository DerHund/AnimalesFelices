from django.shortcuts import render

# Create your views here.
def inicio (request):
    return render(request, 'Tienda/index.html')

def agregarProducto (request):
    return render(request, 'Tienda/agregarProducto.html')

def Articulo (request):
    return render(request, 'Tienda/Articulo.html')

def Carrito (request):
    return render(request , 'Tienda/Carrito.html')

def EditarPerfil (request):
    return render(request, 'Tienda/EditarPerfil.html')

def EditarProducto (request):
    return render(request, 'Tienda/EditarProducto.html')

def EliminarProducto (request):
    return render(request, 'Tienda/EliminarProducto.html')

def gatos (request):
    return render(request, 'Tienda/gatos.html')

def Login (request):
    return render(request, 'Tienda/Login.html')

def Ofertas (request):
    return render(request, 'Tienda/Ofertas.html')

def perros (request):
    return render(request, 'Tienda/perros.html')

def RecuperarContrasena (request):
    return render(request, 'Tienda/RecuperarContrasena.html')

def Registro (request):
    return render(request, 'Tienda/Registro.html')

def VistaAdministrador (request):
    return render(request, 'Tienda/VistaAdministrador.html')