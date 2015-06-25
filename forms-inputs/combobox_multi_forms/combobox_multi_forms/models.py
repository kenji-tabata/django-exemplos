from django.db import models


class Select(models.Model):
    tipo = models.CharField(max_length=100)
    
    def __str__(self):
        return self.tipo