from django.urls import path
from .views import *

urlpatterns = [
    path('home', home, name="home"),
    path('facturas/', facturas, name="facturas"),
    path('boletasVentasPosVentas/', boletasVentasPosVentas, name="boletasVentasPosVentas"),
    path('contable/', contable, name="contable"),
    path('generarLibro/', generarLibro, name="generarLibro"),
    path('perfil/', perfil, name="perfil"),
    path('', iniciosesion, name="iniciosesion"),
]
