Conectando com o banco de dados MySQL com o PyMySQL no Shell
===

Passo-a-passo sobre como criar uma database por linha de comando pelo Shell do Django. Utiliza o mesmo conceito do 
`connection_cursor` do Django para listar, criar, editar e deletar.

Importe o módulo PyMysql

    >>> import pymysql

Crie a conexão com com o banco de dados

    >>> con = pymysql.connect(host='localhost', user='nome-do-usuario', passwd='senha-do-usuario')

Crie o cursor que executará as Query SQL 

    >>> cursor = con.cursor()

Para criar uma database digite:

    >>> cursor.execute('create database dj_testes')

Para selecionar a database digite:

    >>> cursor.execute('use dj_testes')

Para criar uma tabela na database selecionada:

    >>> cursor.execute('create table clientes (id int, nome varchar(255))')