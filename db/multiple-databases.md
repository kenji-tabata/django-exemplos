Multiple databases
===


https://docs.djangoproject.com/en/1.8/topics/db/multi-db/



Neste exemplo é mostrado como funciona o sistema de Multi Database do Django, com ele é possível gerenciar e manipular 
mais de um banco de dados no mesmo sistema. 

O Multi Database do Django funciona de maneira simples, basta adicionar após o objeto Model a função `using('nome-da-base')`, 
por exemplo:

    Post.objects.order_by()    =>   Post.objects.using('default').order_by()
    Post.objects.create()      =>   Post.objects.using('default').create()

Sendo que o parâmetro da função `using()` é o nome (alias) da database definido no arquivo `settings.py`, por exemplo:

    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'exemplos_dj',
        ...
    },



### Instalação do módulo PyMySQL

1. Instale o módulo PyMysql com o comando 

    pip install pymysql

2. Abre o arquivo `__init__.py` e adicione o trecho de código abaixo para ativar o módulo PyMySQL

    import pymysql
    pymysql.install_as_MySQLdb()



### Configuração do Django para o MySQL

1. Abre o arquivo `settings.py`;

2. Procure o seguinte trecho de código:

        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }

3. Substitua pelo código abaixo:

        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'exemplos_dj',
            'USER': 'root',
            'PASSWORD': 'senha-do-root',
            'HOST': '127.0.0.1',
        }

4. Para adicionar as tabelas e criar o usuário admin do Django, digite o comando abaixo.

    python manage.py syncdb



### Configuração do banco de dados

1. Crie as novas tabelas que serão utilizadas pelo Django no MySQL

        exemplos_dj
        exemplos_dj_add

2. Digite o comando abaixo para migrar no `exemplo_dj` do MySQL as tabelas do Django

        python manage.py migrate

3. Adicione a configuração da database `exemplos_dj_add` no arquivo `settings.py`

        'exemplos_dj_add': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'exemplos_dj_add',
            'USER': 'root',
            'PASSWORD': 'senha-do-root',
            'HOST': '127.0.0.1',
        }

4. Adicione a tabela `multi_database_post` na database `exemplos_dj_add` do MySQL, para isso acesse a database 
`exemplos_dj_add` e na aba SQL digite o código abaixo:

        CREATE TABLE IF NOT EXISTS `multi_database_intro_post` (
            `id` int(11) NOT NULL AUTO_INCREMENT,
            `titulo` varchar(200) NOT NULL,
            `conteudo` longtext NOT NULL,
            PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;



### Inserindo registros

Para inserir os registro inicie o Shell do django

### Importe o model do projeto 

    >>> from multi_database_intro.models import Post

### Insere um registro na database `default` digitando o comando abaixo:

    >>> Post.objects.using('default').create(titulo="Testando 1", conteudo="Conteúdo de teste")

### Para Inserir outro registro na database `exemplos_dj_add` digite a mesma linha acima alterando o parâmetro do `using` 
para `exemplos_dj_add`, como no exemplo abaixo:

    >>> Post.objects.using('exemplos_dj_add').create(titulo="Testando 2", conteudo="Conteúdo de teste 2")



Para saber mais como manipular os registros do banco de dados pelo Shell do Django clique no link abaixo:
[Manipulando registros no banco de dados pelo Shell](manipulando-registros-shell/README.md)