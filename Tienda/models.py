from django.db import models

# Create your models here.



class TipoProducto(models.Model):
    idTipoProducto = models.IntegerField(primary_key=True, verbose_name='Código del tipo de producto')
    nombreTipo = models.CharField(max_length=20, verbose_name='Tipo del producto', blank=False, null=False)

    def __str__(self):
        return self.nombreTipo



class Productos(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name= 'Id del producto')
    nombreProducto = models.CharField(max_length=30, verbose_name='Nombre del producto')
    precioProducto = models.IntegerField(verbose_name='Precio del producto')
    cantidadProducto = models.IntegerField(verbose_name='Cantidad del producto')
    descripcionProducto = models.CharField(max_length=500, verbose_name='Descripcion del producto')
    foto = models.ImageField(upload_to="Productos", null= True)
    tipoProducto = models.ForeignKey(TipoProducto,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreProducto


class TipoUsuario(models.Model):
    idTipoUsuario = models.IntegerField(primary_key=True, verbose_name='Código del tipo de usuario')
    nombreTipoUsuario = models.CharField(max_length=20, verbose_name='Tipo de usuario', blank=False, null=False)

    def __str__(self):
        return self.nombreTipoUsuario


class Usuario(models.Model):

    idUsuario = models.IntegerField(primary_key=True, verbose_name= 'Id del usuario')
    nombreUsuario = models.CharField(max_length=30, verbose_name='Nombre del usuario')
    apellidoUsuario = models.CharField(max_length=30, verbose_name='Apellido del usuario')
    claveUsuario = models.CharField(max_length=30, verbose_name='Clave del usuario')
    emailUsuario = models.CharField(max_length=50, verbose_name='Email del usuario')
    telefonoUsuario = models.IntegerField(verbose_name='Telefono del usuario')
    direccionUsuario = models.CharField(max_length=50, verbose_name='Direccion del usuario')
    regionUsuario = models.CharField(max_length=50, verbose_name='Region del usuario')
    comunaUsuario = models.CharField(max_length=50, verbose_name='Comuna del usuario')
    codigoPostalUsuario = models.IntegerField(verbose_name='Codigo postal Usuario')

    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreUsuario