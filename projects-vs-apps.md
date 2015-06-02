Projects vs. apps
===


What’s the difference between a project and an app?

- An __app__ is a Web application that does something – e.g.,
  a Weblog system, a database of public records or a simple poll app.

- A __project__ is a collection of configuration and apps for a particular Web site. 
  A project can contain multiple apps.
  An app can be in multiple projects.


mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app1/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app2/
        __init__.py
        settings.py
        urls.py
        wsgi.py
    app3/
        __init__.py
        settings.py
        urls.py
        wsgi.py



Creating a project
---


    $ django-admin startproject mysite

[1.8/intro/tutorial01/#creating-a-project](https://docs.djangoproject.com/en/1.8/intro/tutorial01/#creating-a-project)



Activating models (apps?)
---

Será um model  equivalente a uma app ?


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