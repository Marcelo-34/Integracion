from django.shortcuts import render

def home(request):
    return render(request, 'app/home.html')

def facturas(request):
    return render(request, 'app/facturas.html')

def boletasVentasPosVentas(request):
    return render(request, 'app/boletasVentasPosVentas.html')

def contable(request):
    return render(request, 'app/contable.html')

def generarLibro(request):
    return render(request, 'app/generarLibro.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def iniciosesion(request):
    return render(request, 'app/iniciosesion.html')