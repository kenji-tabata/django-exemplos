15. Django Forms: Checkbox

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Exemplo de um Checkbox para assinatura de e-mail. 

Arquivos alterados ou adicionados:

    /d15_django_forms_checkbox
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d15_django_forms_checkbox/
            index.html
            enviado.html