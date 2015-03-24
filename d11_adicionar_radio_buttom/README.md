11. Adicionar Radio Buttom

Neste exemplo é mostrado como um radio buttom no próprio template. Exemplo pratico apenas para demonstrar como adicionar
os input radio buttom na página HTML.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /d11_adicionar_radio_buttom/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        d11_adicionar_radio_buttom/
            index.html