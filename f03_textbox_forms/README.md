03. Django Forms: Textbox

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários utilizando o model da aplicação.

Caixas de textos: text, password, email, int, data, url, textarea e decimal.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations f03_textbox_forms
    python manage.py migrate

Arquivos alterados ou adicionados:

    /f03_textbox_forms
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        f03_textbox_forms/
            index.html
            enviado.html