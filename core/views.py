from django.shortcuts import render

# Create your views here.


def home(request):

    return render(request, 'core/home.html')

def sucursal(request):

    return render(request, 'core/sucursales.html')

def galeria(request):

    return render(request, 'core/galeria.html')

def login(request):

    return render(request, 'core/login.html')