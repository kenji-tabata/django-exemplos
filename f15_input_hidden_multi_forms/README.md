15. Django Forms: Input Hidden Multi

Neste exemplo é mostrado como utilizar a classe Forms do Django para criar formulários baseado no model da aplicação.

Exemplo de como enviar varias informações através do input hidden e salvar em um array list.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /f15_input_hidden_multi_forms
        urls.py
        settings.py
        views.py
        models.py
        forms.py
    /templates/
        f15_input_hidden_multi_forms/
            index.html
            enviado.html