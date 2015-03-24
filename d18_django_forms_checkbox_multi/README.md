18. Django Forms: Checkbox Multi

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Exemplo de uma lista de checkbox, onde possível checar vários checkbox e salvar como um array list no banco de dados.

Arquivos alterados ou adicionados:

    /d18_django_forms_checkbox_multi
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d18_django_forms_checkbox_multi/
            index.html
            enviado.html