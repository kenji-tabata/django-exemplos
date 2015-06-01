from django.db import models

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField(max_length=256)
    
    def __str__(self):
        return self.titulo