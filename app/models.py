from django.db import models

import uuid

class Estado_de_la_factua(models.Model):
    Estado_de_la_factua     = models.CharField(max_length=50)

    def __str__(self):
        return self.Estado_de_la_factua

class Facturas(models.Model):
    ID_de_factura           = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    Numero_de_factura       = models.IntegerField()
    fecha_de_emicion        = models.DateField()
    cliente                 = models.CharField(max_length=50)
    Items_de_factura        = models.TextField()
    Total                   = models.IntegerField()
    Estado_de_la_factua     = models.ForeignKey(Estado_de_la_factua, on_delete=models.PROTECT)

    def __str__(self):
        return str(self.ID_de_factura)
    

class Boleta(models.Model):
    Numero_boleta   = models.CharField(max_length=100)
    Fecha_emision   = models.DateField()
    Cliente         = models.CharField(max_length=100)
    Items_boleta    = models.TextField()
    Total           = models.DecimalField(max_digits=10, decimal_places=2)
    Estado          = models.CharField(max_length=50)

    def __str__(self):
        return self.Numero_boleta