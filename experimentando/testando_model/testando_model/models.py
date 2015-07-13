from django.db import models
from django.utils import timezone

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField('E-mail', max_length=250)
    data = models.DateTimeField(default=timezone.now())
    mensagem = models.TextField()
    
    def __str__(self):
        return self.nome