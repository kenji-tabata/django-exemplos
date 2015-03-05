07. Forms

Neste exemplo é mostrado como criamos uma model para armazenar os registros obtidos ao enviar um formulário com o método 
POST.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations nome-da-model
    python manage.py migrate

Arquivos alterados ou adicionados:

    /d07_models/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        d07_models/
            index.html