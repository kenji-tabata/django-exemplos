Adequando os arquivos estáticos (css, imagens, etc..)
===

Segundo a documentação do Django é aconselhável definir a pasta `static` fora da pasta do projeto Django no ambiente de 
produção. Assim todos os arquivos de imagens, css, js e etc estarão isolados do projeto Django evitando problemas de 
segurança.

Os arquivos da pasta static da área de administração, bem como as bibliotecas (Bootstrap) também devem ficar armazenadas 
nesta mesma pasta.

Pasta static da área \admin
---

Nota.: utilize caminhos absolutos.

Crie a pasta para arquivos estáticos

	mkdir /projetos-django/static


No CentOS 5.6
---

1. Adicione no `/etc/httpd/conf/httpd.conf` as seguintes configurações

        Alias /static /projetos-django/static
        <Directory /projetos-django/static>
            Options -Indexes
            Order allow,deny
            Allow from all
        </Directory>


2. Crie um link simbólico para da pasta static/admin do Django

        Com o VirtualEnv desativado:
        # ln -s /usr/local/lib/python3.3/site-packages/django/contrib/admin/static/admin /projetos-django/static/

        Com o VirtualEnv ativado:
        # ln -s /pasta-do-virtualenv/lib/python3.3/site-packages/django/contrib/admin/static/admin /projetos-django/static/

3. Reinicie o Apache

        /etc/init.d/httpd restart

4. Acesse a página `127.0.0.1/nome-do-projeto/admin` e confira o resultado



No Debian 7.5
---

1. Adicione um arquivo de configuração em `etc/apache2/sites-available` com um qualquer nome

        cd /etc/apache2/sites-available
        nano django.conf

2. No arquivo django.conf adicione as seguintes linhas:

        Alias /static /projetos-django/static
        <Directory /projetos-django/static>
            Options -Indexes
            Order allow,deny
            Allow from all
        </Directory>

3. Para habilitar as configurações digite:

        a2ensite django.conf

4. Crie um link simbólico para da pasta static/admin do Django

        Com o VirtualEnv desativado:

        # ln -s /usr/local/lib/python3.3/site-packages/django/contrib/admin/static/admin /projetos-django/static/

        Com o VirtualEnv ativado:

        # ln -s /pasta-do-virtualenv/lib/python3.3/site-packages/django/contrib/admin/static/admin /projetos-django/static/

5. Reinicie o Apache:

        service apache2 restart

6. Acesse a página `127.0.0.1/nome-do-projeto/admin` e confira o resultado



Configurando a pasta Static no Django para o Apache
---

Abre o arquivo `/nome-do-projeto/settings.py` e define a constante STATIC_ROOT para a pasta `static`. Pode ser adicionado 
o PATH absoluto `/home/usuário/projetos/sdd-py/static` ou relativo `os.path.join(os.path.dirname(BASE_DIR), 'static/')`.

        STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static/')

Para copiar todo o conteúdo da pasta `static` do projeto Django para a mesma pasta que contém os arquivos da área admin 
digite:

        python manage.py collectstatic
