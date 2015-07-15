Testando a TEMPLATE no Shell do Python
===

Inicie o Shell do projeto

    python manage.py shell


Testando a VIEW com o Client Test do Django
---

Ative teste Client

    >>> from django.test import Client
    >>> c = Client()

Para visualizar, por exemplo, o conteúdo do template index no shell utilize o seguinte comando:

    >>> resp = c.get('')
    Listar todos os contatos

    >>> resp.content


Para visualizar o HTML do formulário que a Classe `forms.py` gera.

    >>> from testando_template.forms import ContatoForm
    >>> print (ContatoForm())


