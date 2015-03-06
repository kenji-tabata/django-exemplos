from django.db import models

class Radio(models.Model):
    label = models.CharField(max_length=200)
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.label