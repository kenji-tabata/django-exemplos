16. Django Forms: Auto Validar

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

Valida o todos os campos do formulário e caso esteja em branco não envia as informações. Insere as todas as informações 
pelo método save() 

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations f16_auto_validar_forms
    python manage.py migrate

Arquivos alterados ou adicionados:

    /f16_auto_validar_forms/
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        f16_auto_validar_forms/
            index.html
            listar.html