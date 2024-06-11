from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('login', login, name="login"),
    path('camiseta', camisetas, name="camiseta"),
    path('accesorio', accesorios, name="accesorio"),
    path('tour', tours, name="tour"),
    path('vip', vips, name="vip"),
    path('carrito', carrito, name="carrito"),
    path('addToCar/<codigo>', addToCar, name="addToCar"),
    path('delToCar/<codigo>', delToCar, name="delToCar"),
]
