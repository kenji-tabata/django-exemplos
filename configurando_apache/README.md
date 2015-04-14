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
