from django.db import models

class Hidden(models.Model):
    nome = models.CharField(max_length=200)
    dado = models.CharField(max_length=250)
    
    
    def __str__(self):
        return self.nome