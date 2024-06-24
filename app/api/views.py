from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.api.serializers import AppSerializers, AppSerializersB

class FacturasApiViewSet(ModelViewSet):
    serializer_class    = AppSerializers
    queryset = Facturas.objects.all()

class BacturaApiViewSetactura(ModelViewSet):
    serializer_class    = AppSerializersB
    queryset = Boleta.objects.all()