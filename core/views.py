from django.shortcuts import render, redirect
from django.http import Http404
from .models import *
import requests
from .forms import *

# Create your views here.
def home(request):
    id_es = ['0003', '0007','0004','0010']
    cam = Camiseta.objects.filter(codigo__in=id_es)
    return render(request, 'index.html', {'cam': cam})

def tickets (request):
    tkt = Ticket.objects.all()
    return render(request, 'entradas.html',{'tkt':tkt})

def camisetas (request):
    cam = Camiseta.objects.all()
    return render(request, 'camiseta.html', {'cam': cam})

def accesorios (request):
    acc = Accesorio.objects.all()
    return render(request,'accesorio.html', {'acc': acc} )

def tours (request):
    tou = Tour.objects.all()
    return render(request,'tour.html', {'tou': tou})

def zapato (request):
    zapa = Zapatos.objects.all()
    return render(request,'zapatos.html', {'zapa': zapa})

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
                try:
                    producto = Ticket.objects.get(codigo=codigo)
                except Ticket.DoesNotExist:
                    try:
                        producto = Zapatos.objects.get(codigo=codigo)
                    except Zapatos.DoesNotExist:
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
    print("Carrito actualizado:", carrito)  
    return redirect('carrito')  
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
                try:
                    producto = Ticket.objects.get(codigo=codigo)
                except Ticket.DoesNotExist:
                    try:
                        producto = Zapatos.objects.get(codigo=codigo)
                    except Zapatos.DoesNotExist:
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
    print("Carrito actualizado:", carrito)  
    return redirect('carrito')  

def carrito(request):
    carrito = request.session.get('carrito', [])
    total = sum(item['subtotal'] for item in carrito)
    return render(request, 'carrito.html', {
        'carrito': carrito,
        'total': total,
    })
    
def registro(request):
    registro = Registro()
    return render(request, 'registro.html', {'form': registro})