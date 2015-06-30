Configurando o Apache e o Django para executar o projeto no navegador
===

No CentOS 5.6
---

1. Adicione no `/etc/httpd/conf/httpd.conf` as seguintes configurações:

        Com VirtualEnv desativado:

        <VirtualHost *:80>
            WSGIDaemonProcess qualquer-nome python-path=/projetos-django/nome-do-projeto:/usr/local/lib/python3.4/site-packages
            WSGIProcessGroup qualquer-nome
            WSGIScriptAlias /nome-do-projeto /projetos-django/nome-do-projeto/nome-do-projeto/wsgi.py
        </VirtualHost>


        Com VirtualEnv ativado:

        <VirtualHost *:80>
            WSGIDaemonProcess qualquer-nome python-path=/projetos-django/nome-do-projeto:/pasta-do-virtualenv/lib/python3.4/site-packages
            WSGIProcessGroup qualquer-nome
            WSGIScriptAlias /nome-do-projeto /projetos-django/nome-do-projeto/nome-do-projeto/wsgi.py
        </VirtualHost>


2. Reinicie o Apache:

        /etc/init.d/httpd restart


Para ver mensagens do arquivo de LOG do Apache no terminal

        nano /var/log/httpd/error_log



No Debian 7.5
---

1. Crie um arquivo de configuração em sites-avaliable:

        nano /etc/apache2/sites-available/django.conf


2. Adicione as seguintes configurações:

        Com o VirtualEnv desativado:

        WSGIPythonPath /pasta-dos-projetos/nome-do-projeto:/usr/local/lib/python3.4/site-packages
        WSGIScriptAlias /nome-qualquer /pasta-dos-projetos/nome-do-projeto/nome-do-projeto/wsgi.py

        <Directory /pasta-dos-projetos/nome-do-projeto>
            <Files wsgi.py>
                Order deny,allow
                Allow from all
            </Files>
        </Directory>


        Com VirtualEnv ativado:

        WSGIPythonPath /pasta-dos-projetos/nome-do-projeto:/pasta-do-virtualenv/lib/python3.4/site-packages
        WSGIScriptAlias /nome-qualquer /pasta-dos-projetos/nome-do-projeto/nome-do-projeto/wsgi.py

        <Directory /pasta-dos-projetos/nome-do-projeto>
            <Files wsgi.py>
                Order deny,allow
                Allow from all
            </Files>
        </Directory>


3. Habilite a nova configuração com:

        a2ensite django.conf


4. Reinicie o Apache

        service apache2 reload


Nota.: Caso tenha vários projetos Django no servidor Apache, ative com o comando a2ensite para apenas um projeto, evitando 
assim a página de erro 500 (Erro interno no Servidor)

Para ver mensagens do arquivo de LOG do Apache no terminal

        nano /var/log/apache2/error_log
