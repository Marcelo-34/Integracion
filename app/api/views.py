from rest_framework.viewsets import ModelViewSet
from app.models import *
from app.api.serializers import AppSerializers

class FacturasApiViewSet(ModelViewSet):
    serializer_class    = AppSerializers
    queryset = Facturas.objects.all()