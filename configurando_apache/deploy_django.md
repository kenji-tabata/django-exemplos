Como atualizar o site do Django sem reiniciar o Apache
===

Quando atualizamos os arquivos do site no servidor de produção do Apache, pode ocorrer casos que o site não se atualize, 
mesmo usando o Ctrl+f5, o que obriga a reiniciar o servidor para as atualizações entrarem em vigor.

Existe duas maneiras para atualizar o site sem ter que reiniciar o servidor:

A primeira é no terminal utilizando o comando `touch nome-do-projeto/wsgi.py` que irá atualizar o arquivo `wsgi.py` bem 
como o acesso aos novos arquivos adicionados.

A segunda é sobrescrevendo ou salvando novamente o arquivo `wsgi.py`, assim o acesso aos novos arquivos será atualizado no 
servidor Apache.
