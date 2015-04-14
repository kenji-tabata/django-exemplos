Adequando os arquivos estáticos (css, imagens, etc..)
===

Segundo a documentação do Django é aconselhável definir a pasta `static` fora da pasta do projeto Django no ambiente de 
produção. Assim todos os arquivos de imagens, css, js e etc estarão isolados do projeto Django evitando problemas de 
segurança.

Os arquivos da pasta static da área de administração, bem como as bibliotecas (Bootstrap) também devem ficar armazenadas 
nesta mesma pasta.

Pasta static da área \admin
---

Note.: utilize caminhos absolutos.

Crie a pasta para arquivos estáticos

	mkdir /var/www/html/projetos-django/static


Adicione no `/etc/httpd/conf/httpd.conf` as seguites configurações

	Alias /static /var/www/html/projetos-django/static
	<Directory /var/www/html/projetos-django/static>
	    Options -Indexes
	    Order allow,deny
	    Allow from all
	</Directory>


Crie um link simbólico para da pasta static/admin do Django

	ln -s /usr/local/lib/python3.3/site-packages/django/contrib/admin/static/admin /var/www/html/projetos-django/static/


Reinicie o Apache

    /etc/init.d/httpd restart


Acesse a página `127.0.0.1/nome-do-projeto/admin` e confira o resultado



Configurando a pasta Static no Django
---

Abre o arquivo `/nome-do-projeto/settings.py` e define o PATH da pasta `static`. Pode ser adicionado o PATH absoluto 
`/home/usuário/projetos/sdd-py/static` ou relativo `os.path.join(os.path.dirname(BASE_DIR), 'static/')`.

	STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR),'static/')

Para copiar todo o conteúdo da pasta `static` do projeto Django para a mesma pasta que contém os arquivos da área admin 
digite:

	 python manage.py collectstatic
