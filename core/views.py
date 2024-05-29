from django.shortcuts import render

def home(request):
    return render(request, 'index2.html')
def accesorio(request):
    return render(request, 'accesorio.html')
def camiseta(request):
    return render(request, 'camiseta.html')
def entrada(request):
    return render(request, 'entradas.html')
def login(request):
    return render(request, 'iniciar_sesion.html')
def registrarse(request):
    return render(request, 'registrarse.html')
def tour(request):
    return render(request, 'tour.html')
def vip(request):
    return render(request, 'vip22.html')