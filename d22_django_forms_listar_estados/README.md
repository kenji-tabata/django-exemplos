22. Django Forms: Import List

Neste exemplo é mostrado como criamos uma combobox com os estados Brasileiros.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

É preciso instalar o módulo LocalFlavor para alimentar a combobox com os nomes dos Estados do país.

    pip install django-localflavor

Arquivos alterados ou adicionados:

    /d22_django_forms_listar_estados/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        d22_django_forms_listar_estados/
            index.html