14. Django Forms: Textbox

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Caixas de textos: text, password, email, int, data, url, textarea e decimal.

Arquivos alterados ou adicionados:

    /d14_django_forms_textbox
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d14_django_forms_textbox/
            index.html
            enviado.html