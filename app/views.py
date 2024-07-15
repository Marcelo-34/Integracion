import json
from django.shortcuts import render
from .models import Facturas, Boleta
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
import requests
from . import metApi


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
    despachos=metApi.post_ventaApi()
    data = {
    'despachos' : despachos
    }
    
    return render(request, 'app/contable.html', context=data)


def perfil(request):
    return render(request, 'app/perfil.html')

def iniciosesion(request):
    if request.method == 'POST':
        print('Ejecutado con exito')
        username = request.POST.get('username')
        password = request.POST.get('password')
        token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJjb250YWJpbGlkYWQiOiJ0b2tlbl9jb250YWJpbGlkYWQifQ.mRIHsNu0vIu5n-eCc_WtmEZD1-M_IshUhnfs7OhdK3s'
        
        # Datos para la solicitud POST
        payload = json.dumps({
            "username": username,
            "password": password,
            "token": token
        })
        
        headers = {
            'Content-Type': 'application/json'
        }

        # URL del endpoint de validación
        url = 'https://qic534o8o0.execute-api.us-east-1.amazonaws.com/validacionUsuarios/'
        
        try:
            # Realizar la solicitud POST
            response = requests.post(url, headers=headers, data=payload)
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")
            
            if response.status_code == 200:
                print("Inicio de sesion exitoso")
                return redirect('home')
            else:
                messages.error(request, 'Error en la validación de usuario')
                return redirect('iniciosesion')
                
        
        except Exception as e:
            print(f"Exception occurred: {e}")
            messages.error(request, 'Ocurrió un error durante la solicitud de validación')
            return redirect('iniciosesion')
    else:
        return render(request, 'app/iniciosesion.html')

