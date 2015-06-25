from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    cep = models.CharField(max_length=9)
    tel = models.CharField(max_length=13)
    cpf = models.CharField(max_length=14)
    cnpj = models.CharField(max_length=18)
    estados = models.CharField(max_length=20)
    
    def __str__(self):
        return self.tipo