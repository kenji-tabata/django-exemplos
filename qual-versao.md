Qual versão usar?
---


Quando comei a estudar o Django ele estava na versão 1.6, meus primeiros
passos forma nessa versão.

A versão 1.7 estava saindo forno e resolvi utilizá-la no ambiente de produção.

Nesta época, havia a seguinte linha divisória....

+ Django 1.6 trabalha com o Python 2
+ Django 1.7 trabalha com o Python 3

Enquanto trabalho neste repositório a versão 1.8 é a mais atual.


Para saber a versão instalada você pode executar os seguintes comandos.

    $ python
    >>> import django
    >>> print(django.get_version())


Ou, se preferir, ser mais suscinto....

    python -c "import django; print(django.get_version())"


