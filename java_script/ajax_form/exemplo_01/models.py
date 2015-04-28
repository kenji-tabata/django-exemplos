from django.db import models

class Contato(models.Model):
    nome = models.CharField('Nome', max_length= 100)
    telefone = models.CharField('Telefone', max_length= 15, blank=True)
    email = models.EmailField('E-mail', max_length=200)
    
    def __str__(self):
        return self.nome