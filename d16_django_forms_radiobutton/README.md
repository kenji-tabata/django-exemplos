16. Django Forms: Radio Button

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Exemplo de Radio Button para a escolha do sexo. 

Arquivos alterados ou adicionados:

    /d16_django_forms_radiobutton
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d16_django_forms_radiobutton/
            index.html
            enviado.html