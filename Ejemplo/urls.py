
from django.contrib import admin
from django.urls import path
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('accesorios', accesorio, name="accesorio"),
    path('camiseta', camiseta, name="camiseta"),
]
