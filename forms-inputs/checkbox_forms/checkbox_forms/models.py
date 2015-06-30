from django.db import models


class CheckBox(models.Model):
    email = models.EmailField('E-mail')
    assinar = models.CharField('Desejo receber os e-mails', max_length=30, blank=True)
    
    def __str__(self):
        return self.email