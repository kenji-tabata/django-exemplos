from django.db import models

class TextBox(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField('E-mail', max_length=250)
    url = models.URLField('Site')
    data = models.DateTimeField('Data publicada')
    valor = models.DecimalField('Valor R$',max_digits=9, decimal_places=2)
    numero = models.IntegerField('Número')
    mensagem = models.TextField()
    senha = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome