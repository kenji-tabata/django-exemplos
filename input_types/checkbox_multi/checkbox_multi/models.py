from django.db import models

class Check(models.Model):
    nome = models.CharField(max_length=200)
    alternativa = models.CharField(max_length=256)
    
    def __str__(self):
        return self.titulo