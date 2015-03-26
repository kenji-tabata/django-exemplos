from django.db import models
from django.utils import timezone

class Post(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField('Publicado', default=timezone.now)
    conteudo = models.TextField('Conteúdo')
    
    def __str__(self):
        return self.titulo