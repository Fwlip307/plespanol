from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home" ),
    path('registro', registro, name="registro"),
    path('camiseta', camisetas, name="camiseta"),
    path('accesorio', accesorios, name="accesorio"),
    path('tour', tours, name="tour"),
    path('ticket', tickets, name="ticket"),
    path('vip', vips, name="vip"),
    path('carrito', carrito, name="carrito"),
    path('addToCar/<codigo>', addToCar, name="addToCar"),
    path('delToCar/<codigo>', delToCar, name="delToCar"),
    path('zapatos', zapato, name="zapatos"),
    
]
