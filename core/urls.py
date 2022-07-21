from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('autos/', galeria, name="galeria"),
    path('sucursales/', sucursal, name="sucursal"),
    path('login/', login, name="login"),
]
