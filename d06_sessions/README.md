06. Sessions

Neste exemplo é mostrado como utilizar o Sessions do Django.

Faça a migração da tabelas do Django com o comando `python manage.py migrate` para utilizar a Sessions. É necessário ter 
essas tabelas porque o Sessions do Django grava os registros da Session no banco de dados automaticamente.

Arquivos alterados ou adicionados:

    /d06_sessions/
        urls.py
        settings.py
        views.py
    /templates/
        d06_sessions/
            index.html