Qual versão usar?
---

Quando comecei a estudar o Django ele estava na versão 1.6, meus primeiros
passos foram nessa versão.

A versão 1.7 estava saindo do forno e resolvi utilizá-la no ambiente de produção.

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


Dica
===

Quando instalamos o Python 3, normalmente não desinstalamos o Python 2, então
você terá os dois em sua máquina. Experimente...

    $ python -version
    $ python3 -version

Algumas variações podem ser....

    $ python3.2 -version
    $ python3.4 -version

Se estiver usando o Django 1.7, então deverá usar Python 3.

Leia o seguinte artigo para [instalar o Python 3](http://www.devfuria.com.br/linux/cookbook/python/)
