from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def home (request):
    return render(request, 'index.html')

def login (request):
    return render(request, 'iniciar_sesion.html')

def camisetas (request):
    cam = Camiseta.objects.all()
    return render(request, 'camiseta.html', {'cam': cam})

def accesorios (request):
    acc = Accesorio.objects.all()
    return render(request,'accesorio.html', {'acc': acc} )

def tours (request):
    tou = Tour.objects.all()
    return render(request,'tour.html', {'tou': tou})

def vips (request):
    return render(request, 'vip22.html')
def delToCar (request, codigo):
    carrito=request.session.get("carrito",[])
    producto = Accesorio.objects.get(codigo=codigo)
    for item in carrito:
        if item["codigo"] == codigo:
            if item["cantidad"] > 1:
                item["cantidad"]-=1
                item["subtotal"]=item["cantidad"]*item["precio"]
                break
    else:
        carrito.remove(item)


def addToCar (request, codigo):
    carrito=request.session.get("carrito",[])
    producto = Accesorio.objects.get(codigo=codigo)
    for item in carrito:
        if item["codigo"] == codigo:
            item["cantidad"]+=1
            item["subtotal"]=item["cantidad"]*item["precio"]
            break
    else:
        carrito.append({"codigo":codigo, "nombre":producto.detalle, "imagen":producto.imagen,
                    "precio":producto.precio, "cantidad": 1,"subtotal":producto.precio})
    print(carrito)
    request.session["carrito"]=carrito
    # request.session.flush()
    return redirect(to="accesorio") 

def carrito(request):
    return render(request, "carrito.html")