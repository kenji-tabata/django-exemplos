Integrando com uma base de dados legada
===

https://docs.djangoproject.com/en/1.8/howto/legacy-databases/

Passo-a-passo sobre como importar o `Model` de uma base de dados já existente do MySQL para o Django. 

Configure uma nova conexão da base de dados com os dados da base de dados existente.
    
    'nome-da-conexão-da-base-de-dados': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome-da-base-de-dados-do-mysql',
        'USER': '[usuário]',
        'PASSWORD': '[senha]',
        'HOST': '127.0.0.1'
    },

Para visualizar o `model` que será criado da base de dados externa

    $ python manage.py inspectdb --database='nome-da-conexao-da-base-de-dados'

Para importar o `model` da  base de dados externa

    $ python manage.py inspectdb --database='nome-da-conexao-da-base-de-dados' > models.py

Por padrão o Django não permite a manipulação (adicionar, alterar ou deletar) das tabelas importadas.

Para permitir a manipulação destas tabelas altere para `True` o `managed` ou remova-o da classe.

    class Person(models.Model):
        id = models.IntegerField(primary_key=True)
        first_name = models.CharField(max_length=70)
        class Meta:
           managed = True 
           db_table = 'nome_da_tabela_no_banco'

Após criado o arquivo `models.py` importe para a base de dados do Django

    $ python manage.py migrate
