Projects vs. apps
===

Qual a diferença entre um projeto (projetct) e uma aplicação (app)?

- Uma __app__ é uma aplicação web que faz alguma coisa, por exemplo:
  um sitema de weblog, um banco de dados de registros públicos (database of public records)
  ou um simples aplicação de enquetes (simple poll app).

- Um __project__ é uma coleção de configuração e aplicativos (app) para um Web site em particular.
  
Um projeto pode ter múltiplos apps

Uma app pode estar em múltiplos projetos

Veja a documentação [1.8/intro/tutorial01/#creating-models](https://docs.djangoproject.com/en/1.8/intro/tutorial01/#creating-models)

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

Para incluirmos uma app no projeto executamos...

    $ cd mysite
    $ django-admin startapp app1

Após incluirmos algumas apps, nossa estrutura será modificada como se segue.

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

As app's são ativados alterando o arquivo `mysite/settings.py` conforme exemplo abaixo.

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