02. Textbox

Neste exemplo é mostrado como renderizar um formulário simples com textbox utilizando HTML puro, a VIEW fica somente 
responsável por receber e armazenar os dados. 

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations f02_textbox
    python manage.py migrate

Arquivos alterados ou adicionados:

    /f02_textbox/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        f02_textbox/
            index.html