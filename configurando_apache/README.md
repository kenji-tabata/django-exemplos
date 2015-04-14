Configurando o Apache e o Django do Debian para executar o projeto
===

Crie um arquivo de configuração em sites-avaliable:

    nano /etc/apache2/sites-available/exemplo.conf


Adicione as seguintes configurações:
    
    WSGIPythonPath /pasta-dos-projetos/nome-do-projeto:/pasta-do-virtualenv/lib/python3.4/site-packages
    WSGIScriptAlias /nome-qualquer /pasta-dos-projetos/nome-do-projeto/nome-do-projeto/wsgi.py

    <Directory /pasta-dos-projetos/nome-do-projeto>
        <Files wsgi.py>
            Order deny,allow
            Allow from all
        </Files>
    </Directory>


Habilite a nova configuração com:

    a2ensite exemplo.conf


Reinicie o Apache

    service apache2 reload


Para ver mensagens do arquivo de LOG do Apache no terminal

    nano /var/log/apache2/error_log




Tratando o erro "attempt to write a readonly database" e "unable to open database file"
===

Caso utilize a database do Django para realizar os testes (db.sqlite3) é necessário alterar as permissões e o grupo da 
pasta do projeto e do arquivo db.sqlite3, seguido os seguintes passos.

O projeto `Try Except` está utilizando essa configuração para executar no servidor Apache.

Altere o grupo da pasta do projeto:

    chgrp www-data nome-do-projeto

E suas permissões:

    chmod g+w nome-do-projeto

Altere o grupo do arquivo db.sqlite3:

    chgrp www-data db.sqlite3

E suas permissões:

    chmod g+w db.sqlite3

[Saiba mais](http://fredericiana.com/2014/11/29/sqlite-error-open-database-file/)