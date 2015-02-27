Exemplos Django
===

Contém diversos exemplos práticos de aplicações que auxiliam no desenvolvimento de projetos desenvolvidos no Django, 
começando desde o básico ao criar uma página com "Hello World" e indo até a utilização de módulos como Reportlab e Pillow.

O Objetivo é mais para utilizar como uma fonte de informações sobre o que fazer para criar uma determinada parte do site,
como formulários, criar arquivos pdf, adicionar imagens e entre outros.



Índice
---

    01. [Criando uma página Hello World](dj_01_hello_world)



Configurações básicas utilizadas
---

Abaixo estão as configurações utilizadas que facilitam no desenvolvimento do site, elas já foram aplicadas neste projeto
e estão aqui mais como informação sobre como fazer caso crie um outro projeto com as mesmas configurações deste projeto.


###Pasta padrão para os templates HTML

    1. Crie uma nova pasta na raiz do projeto com o nome `template`;
    2. Adicione no arquivo `settings.py` a seguinte configuração: `TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]`;
    3. Todo template criado deve ser colocado em uma pasta com o mesmo nome da aplicação.


###Configuração do Banco de Dados MySQL

    1. Para trocar o Banco de Dados utilizado no projeto abre o arquivo `settings.py`;
    2. Procure o seguinte trecho de código:

        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': 'mydatabase',
        }

    3. E substitua pelo código abaixo:

        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nome-da-database',
            'USER': 'root',
            'PASSWORD': 'senha-do-root',
            'HOST': '127.0.0.1',
        }

    4. Instale o módulo PyMysql com o comando `pip install pymysql`;

    5. Por último abre o arquivo `__init__.py` e adicione o trecho de código abaixo para ativar o módulo PyMySQL

        import pymysql
        pymysql.install_as_MySQLdb()