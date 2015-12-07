from django.db import models
from django.utils import timezone

class Formulario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=11)
    preenchido = models.DateTimeField('Data do Preenchimento',default=timezone.now())
    nasc = models.DateField('Data de Nascimento')
    sexo = models.CharField(max_length=4)
    email = models.EmailField('E-mail', max_length=100)
    ddd = models.CharField('DDD', max_length=2)
    telefone = models.CharField(max_length=10)
    end = models.CharField('Endereço', max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField('CEP', max_length=9)
    resp = models.CharField('Resposta', max_length=100)
#    formularios = models.ManyToManyField(Pessoa, through="Grupo", through_fields=('formulario','pessoa'))
    
class Pessoa(models.Model):
    dado = models.CharField(max_length=200)
    grupos = models.ManyToManyField(Formulario, through="Grupo", through_fields=('pessoa', 'formulario'))
    
class Grupo(models.Model):
    formulario = models.ForeignKey(Formulario)
    pessoa = models.ForeignKey(Pessoa)
    