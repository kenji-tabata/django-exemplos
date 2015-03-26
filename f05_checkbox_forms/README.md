05. Django Forms: Checkbox

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

Exemplo de um Checkbox para assinatura de e-mail. 

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations f05_checkbox_forms
    python manage.py migrate


Arquivos alterados ou adicionados:

    /f05_checkbox_forms
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        f05_checkbox_forms/
            index.html
            enviado.html