from django.db import models

class Post(models.Model):
    label = models.CharField(max_length=200)
    valor = models.CharField(max_length=250)
    
    def __str__(self):
        return self.label