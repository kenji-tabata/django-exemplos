Testando o template gerado pelo Forms no Shell do Python
===

Antes de tudo precisamos criar o Forms...

```
"""  mysite/polls/forms.py """
from django import forms
from mysite.models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = '__all__'
```

... e criar seu modelo.

```
"""  mysite/polls/models.py """
from django.db import models
from django.utils import timezone

class Contato(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField('E-mail', max_length=250)
    data = models.DateTimeField()
    mensagem = models.TextField()
    
    def __str__(self):
        return self.nome
```


### No terminal

Inicie o Shell do projeto.

    $ python manage.py shell
    >>> from django.test import Client
    >>> c = Client()

Para visualizar o HTML do formulário gerado pela classe `forms.py` execute os comandos abaixo.

    >>> from testando_template.forms import ContatoForm
    >>> print (ContatoForm())

O resultado é...

```html
<tr><th><label for="id_nome">Nome:</label></th><td><input id="id_nome" maxlength="200" name="nome" type="text" /></td></tr>
<tr><th><label for="id_email">E-mail:</label></th><td><input id="id_email" maxlength="250" name="email" type="email" /></td></tr>
<tr><th><label for="id_data">Data:</label></th><td><input id="id_data" name="data" type="text" /></td></tr>
<tr><th><label for="id_mensagem">Mensagem:</label></th><td><textarea cols="40" id="id_mensagem" name="mensagem" rows="10">
</textarea></td></tr>
```