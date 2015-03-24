23. Django Forms: Auto Validar

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations d23_django_forms_auto_validar
    python manage.py migrate

Valida o todos os campos do formulário e caso esteja em branco não envia as informações. Insere as todas as informações 
pelo método save() 

Arquivos alterados ou adicionados:

    /d23_django_forms_auto_validar/
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        d23_django_forms_auto_validar/
            index.html
            listar.html