from django.db import models

class Radio(models.Model):
    sexo = models.CharField(max_length=10)
    
    def __str__(self):
        return self.sexo