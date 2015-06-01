from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    
    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario)
    mensagem = models.TextField()
    
    def __str__(self):
        return self.mensagem