from django.shortcuts import render, redirect
from django.http import Http404
from .models import *

# Create your views here.
def home (request):
    return render(request, 'index.html')

def login (request):
    return render(request, 'iniciar_sesion.html')

def entradas (request):
    return render(request, 'entradas.html')

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
def addToCar(request, codigo):
    carrito = request.session.get("carrito", [])
    producto = None

    try:
        producto = Accesorio.objects.get(codigo=codigo)
    except Accesorio.DoesNotExist:
        try:
            producto = Camiseta.objects.get(codigo=codigo)
        except Camiseta.DoesNotExist:
            try:
                producto = Tour.objects.get(codigo=codigo)
            except Tour.DoesNotExist:
                raise Http404("Producto no encontrado")

    for item in carrito:
        if item["codigo"] == codigo:
            item["cantidad"] += 1
            item["subtotal"] = item["cantidad"] * item["precio"]
            break
    else:
        carrito.append({
            "codigo": codigo,
            "nombre": producto.detalle,
            "imagen": producto.imagen,
            "precio": producto.precio,
            "cantidad": 1,
            "subtotal": producto.precio
        })

    request.session["carrito"] = carrito
    print("Carrito actualizado:", carrito)  # Mensaje de depuración
    return redirect('carrito')  # Asegúrate de que esta vista exista y sea correcta
def delToCar(request, codigo):
    carrito = request.session.get("carrito", [])
    producto = None

    try:
        producto = Accesorio.objects.get(codigo=codigo)
    except Accesorio.DoesNotExist:
        try:
            producto = Camiseta.objects.get(codigo=codigo)
        except Camiseta.DoesNotExist:
            try:
                producto = Tour.objects.get(codigo=codigo)
            except Tour.DoesNotExist:
                raise Http404("Producto no encontrado")

    item_to_remove = None

    for item in carrito:
        if item["codigo"] == codigo:
            if item["cantidad"] > 1:
                item["cantidad"] -= 1
                item["subtotal"] = item["cantidad"] * item["precio"]
            else:
                item_to_remove = item
            break

    if item_to_remove:
        carrito.remove(item_to_remove)

    request.session["carrito"] = carrito
    print("Carrito actualizado:", carrito)  # Mensaje de depuración
    return redirect('carrito')  # Asegúrate de que esta vista exista y sea correcta

def carrito(request):
    return render(request, 'carrito.html', {
        'carrito': request.session.get('carrito', [])
    })