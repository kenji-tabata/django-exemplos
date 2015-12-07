from django.db import models

class Transportes(models.Model):
    carro     = models.CharField(max_length=50, blank=True, null=True)
    moto      = models.CharField(max_length=50, blank=True, null=True)
    onibus    = models.CharField(max_length=50, blank=True, null=True)
    bicicleta = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)