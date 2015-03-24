09. Adicionar Checkbox

Neste exemplo é mostrado como adicionar um checkbox no próprio template. Exemplo pratico apenas para demonstrar como 
adicionar input do radio buttom na página HTML.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /d09_adicionar_checkbox/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        d09_adicionar_checkbox/
            index.html