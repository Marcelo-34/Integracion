from rest_framework.serializers import ModelSerializer
from app.models import *

class AppSerializers(ModelSerializer):
    class Meta:
        model = Facturas
        fields = ('ID_de_factura', 'Numero_de_factura', 'fecha_de_emicion', 'cliente', 'Items_de_factura', 'Total', 'Estado_de_la_factua')