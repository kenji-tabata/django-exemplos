19. Django Forms: Select Multi

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Exemplo de uma lista por combobox, onde possível checar vários itens e salvar como um array list no banco de dados.

Arquivos alterados ou adicionados:

    /d19_django_forms_select_multi
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d19_django_forms_select_multi/
            index.html
            enviado.html
