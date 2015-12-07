from django.db import models

class Transportes(models.Model):
    opcoes_transp = models.CharField(max_length=50, blank=True, null=True)
    
    def __str__(self):
        return str(self.id)