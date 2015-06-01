Models
===


Criando um modelo
---


===



Como ativar (activating) um modelo Modelo
---

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




O comando makemigrations
---


    python manage.py makemigrations models


O comando migrate
---

    python manage.py migrate






