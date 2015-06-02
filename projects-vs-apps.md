Projects vs. apps
===


What’s the difference between a project and an app?

- An __app__ is a Web application that does something – e.g.,
  a Weblog system, a database of public records or a simple poll app.

- A __project__ is a collection of configuration and apps for a particular Web site. 
  A project can contain multiple apps.
  An app can be in multiple projects.


Para criar um projeto executamos...

    $ django-admin startproject mysite

Onde `mysite` será o nome e a pasta de seu projeto.

Após a execução do comando teremos uma estrutura semelhante a exibida abaixo.

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py

Após incluirmos algumas appas nossa estrutura será parecida com a seguinte.

    mysite/
        manage.py
        mysite/
            __init__.py
            settings.py
            urls.py
            wsgi.py
        app1/
        app2/
        app3/

Os modelos são ativados alterando o arquivo `mysite/settings.py` conforme exemplo abaixo.

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'app1',
        'app2',
        'app3',        
    )


Será um model equivalente a uma app ?
