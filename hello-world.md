Hello world
===

Crie o projeto em sua pasta de projetos.

    django-admin startproject mysite
    cd mysite/ 

Inicie o banco de dados e o servidor embutido.

    python manage.py migrate
    python manage.py runserver

Acesse através de seu navegador o endereço [http://localhost:8000/](http://localhost:8000/).


Sua primeira view
---

Atualize o arquivo `mysite/mysite/urls.py` conforme abaixo.

```python
from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```

Crie o arquivo `mysite/mysite/views.py` e insira o seguinte.

```python
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world.")
```

Novamente, acesse o endereço [http://localhost:8000/](http://localhost:8000/).



Seu primeiro template
===

O Django buscará os templates na pasta `templates` e, por tanto, temos que avisá-lo. Vamos alterar o trecho do arquivo
`mysite/mysite/settings.py` conforme demosntrado abaixo:

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'], # ,<------- ATENÇÂO
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

Continuando, na pasta `mysite/` crie uma pasta chamada `templates`.

    cd mysite/
    mkdir templates

A pasta `templates` conterá todos os arquivos de template de seu projeto.

Cada app deve ter a sua pasta, então temos que criar a pasta `mysite`.

    cd templates/
    mkdir mysite

Sua estrutura de arquivo deve ser semelhante a esta.

    mysite/
        mysite/
        templates/
            mysite/
        manage.py

E, finalmente, criarmos nosso template `mysite/templates/myite/index.html`.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Hello World</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Hello World</h1>
    </body>
</html>
```

Mais uma vez, acesse o endereço [http://localhost:8000/](http://localhost:8000/).
