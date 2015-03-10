from django.db import models


class CheckBox(models.Model):
    email = models.EmailField('E-mail')
    assinar = models.CharField('Assinar', max_length=10, blank=True)
    
    def __str__(self):
        return self.email