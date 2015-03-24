20. Django Forms: Input Hidden 

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Exemplo de como enviar uma informação através do input hidden.

Arquivos alterados ou adicionados:

    /d20_django_forms_input_hidden
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d21_django_forms_input_hidden/
            index.html
            enviado.html