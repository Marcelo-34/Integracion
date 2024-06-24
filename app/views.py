from django.shortcuts import render
from .models import Facturas, Boleta

def home(request):
    return render(request, 'app/home.html')

def facturas(request):
    Factura = Facturas.objects.all()
    data = {
        'Factura': Factura
        }

    return render(request, 'app/facturas.html', data)

def boletasVentasPosVentas(request):
    boleta = Boleta.objects.all()
    data = {
        'boleta': boleta
        }

    return render(request, 'app/boletasVentasPosVentas.html',data)

def contable(request):
    return render(request, 'app/contable.html')

def generarLibro(request):
    return render(request, 'app/generarLibro.html')

def perfil(request):
    return render(request, 'app/perfil.html')

def iniciosesion(request):
    return render(request, 'app/iniciosesion.html')