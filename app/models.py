from django.db import models

class facturas(models.Model):
    cliente                 = models.CharField(max_length=50)
    numero_de_factura       = models.IntegerField()
    monto                   = models.IntegerField()
    termino_en_dias         = models.IntegerField()
    fecha_de_vencimiento    = models.DateField()
    esta_pagodo             = models.CharField(max_length=50)
    estado                  = models.TextField()

    def __str__(self):
        return self.cliente