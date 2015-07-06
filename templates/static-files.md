Arquivos Estáticos (CSS, JS, Imagens e etc)
===


[https://docs.djangoproject.com/en/dev/howto/static-files/](https://docs.djangoproject.com/en/dev/howto/static-files/)


```html
{% load staticfiles %}
<!DOCTYPE html>
<html>
    <head>
        <title>Static Files</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="{% static 'css/style.css' %}"/>
        <script type="text/javascript" src="{% static 'js/script.js' %}"></script>
    </head>
    <body>
    </body>
</html>
```

Comentar sobre a constante abaixo...(uma pasta para todas as apps)

    STATIC_URL = '/static/'

Crie uma pasta chamada `static` na pasta raiz do projeto:

    mkdir nome-do-projeto/static

No arquivo `settings.py` adicione as linhas abaixo para definir o PATH da pasta static do projeto Django.

    STATICFILES_DIRS = (
        os.path.join(BASE_DIR, "static"),
    )


Para o template reconhecer a utilização dos arquivos estáticos, adicione na primeira linha do HTML a linha abaixo:

    {% load staticfiles %}

Assim quando for adicionar um arquivo estático no template, adicione no path do arquivo a sinha abaixo:

    {% static 'nome-da-pasta/nome-do-arquivo.extensão' %}

    Ex.: <img src="{% static 'imagem/logo.png' %}" alt='logo' title='DOM'/>


Por questões de segurança é aconselhável definir a pasta static do Apache em um local diferente do projeto Django, mas é 
possível definir a mesma pasta para os dois servidores.




No Apache
---

Crie uma nova pasta fora do projeto Django para os arquivos estáticos do Apache

    mkdir static

No arquivo `settings.py` adicione as linhas abaixo para definir o PATH da pasta static do Apache, no exemplo abaixo a 
pasta static está fora da projeto django

    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static/')

Configure o Apache para ter permissão de acesso a pasta static:

No CentOS adicione as linhas abaixo no arquivo `/etc/httpd/conf/httpd.conf`

    Alias /static /projetos-django/static
    <Directory /projetos-django/static>
        Options -Indexes
        Order allow,deny
        Allow from all
    </Directory>

No Debian adicione as linhas abaixo no arquivo de configuração do site, exemplo django.conf

    Alias /static /projetos-django/static
    <Directory /projetos-django/static>
        Options -Indexes
        Order allow,deny
        Allow from all
    </Directory>

Reinicie o Apache

    No CentOS: /etc/init.d/httpd restart
    No Debian: service apache2 restart

Para copiar os arquivos estáticos do projeto para a pasta do Apache digite a linha abaixo

    python manage.py collectstatic

Quando colocar o site no servidor de produção envie somente a pasta static que foi configurada pelo Apache (aquele que 
estará fora da pasta do projeto) evitando assim duplicar os arquivos no servidor. 
