Experimentando a PAI (terminal)
===


[Playing with the API](https://docs.djangoproject.com/en/1.7/intro/tutorial01/#playing-with-the-api)


Após ter migrado as tabelas da aplicação utilize o Shell do Django e digite as linha abaixo para inserir um registro no 
banco de dados da aplicação. Para ver todos os registros cadastrados acesse a página index do projeto.

    # Importe o model do projeto
    >>> from models.models import Post

    # Importe o módulo de data e hora do Django
    from datetime import datetime
 
    # Para inserir um objeto Post (registro)
    Post.objects.create(titulo="Teste de notas", data=datetime.now(), conteudo="Bloco de texto")

    # Para visualizar no Shell todos os objetos cadastrados digite:
    >>> Post.objects.all()