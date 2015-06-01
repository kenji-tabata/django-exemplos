from django.db import models
from django.utils import timezone

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField(max_length=150)
    data = models.DateTimeField('Criado em',default=timezone.now)
    status = models.CharField(max_length=100)
    
    class Meta:
        ordering = ('-id',)
    
    def __str__(self):
        return self.nome
    
    
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario)
    assunto = models.CharField(max_length=200)
    data = models.DateTimeField(default=timezone.now)
    msg = models.TextField('Mensagem')
    
    def __str__(self):
        return self.assunto