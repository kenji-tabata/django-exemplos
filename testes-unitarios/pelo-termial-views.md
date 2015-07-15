Testando as Views no Shell do Python
===

https://docs.djangoproject.com/en/1.8/intro/tutorial05/#test-a-view

A documentação fala que é preciso executar o `setup_test_environment` mas eu não vi diferença quando não executado.

    $ python manage.py shell 
    >>> from django.test.utils import setup_test_environment
    >>> setup_test_environment()

Para todos os exemplos de testes com request utilize o código abaixo para importar o teste do cliente

    >>> from django.test import Client
    >>> c = Client()
    >>> response = client.get('/')
    >>> # we should expect a 404 from that address
    >>> response.status_code
    404
    >>> # on the other hand we should expect to find something at '/polls/'
    >>> # we'll use 'reverse()' rather than a hardcoded URL
    >>> from django.core.urlresolvers import reverse
    >>> response = client.get(reverse('polls:index'))
    >>> response.status_code
    200
    >>> response.content