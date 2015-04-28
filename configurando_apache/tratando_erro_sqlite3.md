Tratando o erro "attempt to write a readonly database" e "unable to open database file"
===

Caso utilize a database do Django para realizar os testes (db.sqlite3) é necessário alterar as permissões e o grupo da 
pasta do projeto e do arquivo db.sqlite3, seguido os seguintes passos.

O projeto `introducao/try_except` está utilizando essa configuração para executar no servidor Apache com SQLite3.

Altere o grupo da pasta do projeto:

    chgrp www-data nome-do-projeto

E suas permissões:

    chmod g+w nome-do-projeto

Altere o grupo do arquivo db.sqlite3:

    chgrp www-data db.sqlite3

E suas permissões:

    chmod g+w db.sqlite3

[Saiba mais](http://fredericiana.com/2014/11/29/sqlite-error-open-database-file/)