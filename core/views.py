from django.shortcuts import render
from .models import *
# Create your views here.


def home(request):

    return render(request, 'core/home.html')

def sucursal(request):
    sucursales = Sucursal.objects.all()
    data = {
        'sucursales': sucursales
    }
    return render(request, 'core/sucursales.html', data)

def galeria(request):
    vehiculos = Vehiculo.objects.all()
    data = {
        'vehiculos': vehiculos
    }
    return render(request, 'core/galeria.html', data)


def listarClientes(request):
    clientes = Clientes.objects.all()
    data = {
        'clientes':clientes
    }
    return render(request, 'core/clientes/listar.html', data)


def login(request):

    return render(request, 'core/login.html')

