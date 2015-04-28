Alterando as permissões da pasta para o Apache acessar
===

Para o servidor Apache acessar e escrever arquivos em uma determinada pasta é preciso atribuir as permissões de escrita 
para o grupo do Apache na pasta.

No Debian
---

Altere o grupo da pasta com o comando abaixo:

    chgrp www-data nome-do-arquivo-ou-pasta

E altere as permissões dos arquivos e pastas para o Apache acessar

    chmod g+w nome-do-arquivo-ou-pasta
