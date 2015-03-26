01. Models

Neste exemplo é mostrado como criamos um model do projeto.

No arquivo `settings.py` é adicionado o model do projeto no `INSTALLED_APPS` para criar as tabelas do arquivo `models.py`.

Para criar a tabela do Model digite no terminal os seguintes comandos:

    python manage.py makemigrations f01_models
    python manage.py migrate

Após ter migrado as tabelas da aplicação utilize o Shell do Django e digite as linha abaixo para inserir um registro no 
banco de dados da aplicação. Para ver todos os registros cadastrados acesse a página index do projeto.

    # Importe o model do projeto
    >>> from f01_models.models import Post

    # Importe o módulo de data e hora do Django
    from datetime import datetime
 
    # Para inserir um objeto Post (registro)
    Post.objects.create(titulo="Teste de notas", data=datetime.now(), conteudo="Bloco de texto")

    # Para visualizar no Shell todos os objetos cadastrados digite:
    >>> Post.objects.all()

Arquivos alterados ou adicionados:

    /f01_models/
        urls.py
        settings.py
        views.py
        models.py
    /templates/
        f01_models/
            index.html