from django.db import models
from django.utils import timezone
import re

class Formulario(models.Model):
    nome = models.CharField(max_length=200)
    cpf = models.CharField(max_length=14)
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
    
    def returnNumero(self):
        num = re.sub("[-\. ]", "", self)
        return num
    
    def verificaCPF(self):
        if len(self) < 11:
            return True
        return False
    
    def numeroRepetidos(self):
        rep = 0
                
        for digito in range(len(self)-2):
            if self[digito] == self[digito + 1]:
                # print(self[digito])
                rep = rep+1
                
        # print(rep)
        
        return rep
    
    
    def verificarDdd(self):
        if re.match(r'\d{2}', self):
            return True
        return False
    
    def verificarTelefone(self):
        if re.match(r'\d{4,5}-\d{4}', self):
            return True
        return False
    
    def verificarCep(self):
        if re.match(r'\d{5}-\d{3}', self):
            return True
        return False
        