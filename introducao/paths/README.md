Django PATHs
===

O arquivo `settings.py` permite definir constantes como caminhos relativos (PATH) evitando a utilização de caminhos absolutos 
de arquivos nas views e templates.

Por padrão um projeto Django já vem definido duas constantes utilizadas pelo sistema:

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    =>  Pasta raiz do projeto

    STATIC_URL = '/static/'                                 
    =>  Pasta para os arquivos estáticos (CSS, JS, Imagens e etc)

    TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
    =>  Pasta para os templates do projeto


Define a constante no `settings.py`
---

Para definir uma constate de uma pasta que está na pasta raiz do projeto utilize:

    NOVA_CONSTANTE = [os.path.join(BASE_DIR, 'nova_pasta')]
    
    O `os.path.join` irá concatenar o caminho da pasta raiz com o nome da pasta.

Para definir a constate de uma pasta que está fora da pasta raiz do projeto utilize:

    PASTA_LINKS = os.path.join(os.path.dirname(BASE_DIR), 'links')

    O `os.path.dirname(BASE_DIR)` irá voltar uma pasta acima do projeto `paths`, retornando assim para a pasta `intoducao`.


Utilizando a constate nos arquivos Python
---

A constante pode ser utilizada em qualquer arquivo Python do projeto. Primeiro faça o importe do arquivo de configuração 
do projeto:

    from django.conf import settings

Uma maneira para verificar qual o caminho que está configurado na constante é utilizando o comando abaixo:

    print ('%s/texto.txt' % settings.NOVA_PASTA)

O resultado seria o caminho absoluto do arquivo

    /projetos/django-exemplos/introducao/paths/nova_pasta/texto.txt
