from django.db import models

class Combobox(models.Model):
    estado = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipo