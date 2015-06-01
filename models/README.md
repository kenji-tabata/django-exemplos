Como ativar (activating) um modelo Modelo
===

Neste exemplo é mostrado como ativamos um model do projeto.


1. No arquivo `[projeto]/settings.py` é adicionado o model do projeto na tupla [INSTALLED_APPS](https://docs.djangoproject.com/en/1.7/ref/settings/#std:setting-INSTALLED_APPS).

[projeto]/settings.py

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
)




para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations models
    python manage.py migrate

Após ter migrado as tabelas da aplicação utilize o Shell do Django e digite as linha abaixo para inserir um registro no 
banco de dados da aplicação. Para ver todos os registros cadastrados acesse a página index do projeto.

    # Importe o model do projeto
    >>> from models.models import Post

    # Importe o módulo de data e hora do Django
    from datetime import datetime
 
    # Para inserir um objeto Post (registro)
    Post.objects.create(titulo="Teste de notas", data=datetime.now(), conteudo="Bloco de texto")

    # Para visualizar no Shell todos os objetos cadastrados digite:
    >>> Post.objects.all()
