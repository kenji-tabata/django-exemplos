from django.db import models

class Combobox(models.Model):
    tipo = models.CharField(max_length=20)
    
    def __str__(self):
        return self.label