from django.db import models

class Assinatura(models.Model):
    email = models.CharField(max_length=200)
    assina = models.CharField(max_length=250)
    
    def __str__(self):
        return self.label