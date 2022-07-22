
from distutils.command.upload import upload
from django.db import models

# Create your models here.


class Sucursal(models.Model):
    idSucursal = models.IntegerField(primary_key=True, verbose_name='sucursal id: ')
    region = models.CharField(max_length=100, verbose_name='region')
    comuna = models.CharField(max_length=100, verbose_name='comuna')
    direccion = models.CharField(max_length=100, verbose_name='direccion')
    imagen = models.ImageField(upload_to = "sucursales", null= True)

    ###

    def __str__(self):
        return self.comuna

# Create your models here.
class Clientes(models.Model):
    rutCliente = models.IntegerField(primary_key=True,verbose_name='rut_cliente')
    nombreCliente = models.CharField(max_length=50,verbose_name="Nombre del Cliente")

    def __str__(self):
        return self.nombreCliente

class Vehiculo(models.Model):
    idVehiculo=models.IntegerField(primary_key=True,verbose_name='Id del vehiculo')
    patente= models.CharField(max_length=6,verbose_name='Patente')
    marca=models.CharField(max_length=20, verbose_name='Marca vehiculo')
    modelo= models.CharField(max_length=20,null=True,blank=True,verbose_name='Modelo')
    color=models.CharField(max_length=20,verbose_name='Color vehiculo')
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to = "vehiculos", null= True)
    def __str__(self) :
        return self.patente


class Vendedores(models.Model):
    rutVendedor = models.IntegerField(primary_key=True,verbose_name='rut_vededor')
    nombreVendedor = models.CharField(max_length=50,verbose_name="Nombre del vendedor")
    def __str__(self):
        return self.nombreVendedor

class Ventas(models.Model):
    idVenta= models.IntegerField(primary_key=True, verbose_name='Id venta')
    cantidadVenta= models.IntegerField(blank=True,null=True)
    vendedor = models.ForeignKey(Vendedores,on_delete=models.CASCADE)
    Vehiculo = models.ForeignKey(Vehiculo,on_delete=models.CASCADE)
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    
    def __str__(self) :
        return self.idVenta