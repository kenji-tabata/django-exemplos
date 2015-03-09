10. Checkbox Multi

Neste exemplo é mostrado como armazenar no banco de dados as alternativas selecionadas por checkbox

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /d10_checkbox_multi/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        d10_checkbox_multi/
            index.html