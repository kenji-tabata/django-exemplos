from django.db import models
from django.utils import timezone

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField('Publicado', default=timezone.now)
    email = models.EmailField('E-mail', max_length=250)
    url = models.URLField('Site')
    rating = models.DecimalField(max_digits=9, decimal_places=1)
    like = models.IntegerField()
    conteudo = models.TextField('Conteúdo')
    
    def __str__(self):
        return self.titulo