21. Django Forms: Input Hidden Multi

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Exemplo de como enviar varias informações através do input hidden e salvar em um array list.

Arquivos alterados ou adicionados:

    /d21_django_forms_input_hidden_multi
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d21_django_forms_input_hidden_multi/
            index.html
            enviado.html