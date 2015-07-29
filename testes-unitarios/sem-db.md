Testes Unitários sem Bando de Dados
===

Como executar testes unitários sem iniciar o bando de dados?

Fontes:

- http://stackoverflow.com/questions/5917587/django-unit-tests-without-a-db
- http://w3facility.org/question/django-unit-tests-without-a-db/

Para executar testes unitários sem inicializar o banco de dados e, por tanto, executar os testes de forma mais rápida
precisamos sobrescrever os métodos de inicialização do banco de dados da classe `DiscoverRunner` (versão 1.8).

Quando executarmos os testes devemos especificar que utilizaremos o arquivo de configuração abaixo.

```python
""" mysite/settings_noDB.py """
from django.test.runner import DiscoverRunner

class TestRunnerWithoutDB(DiscoverRunner):
  def setup_databases(self, **kwargs):
    pass

  def teardown_databases(self, old_config, **kwargs):
    pass
```

Vamos ver se está funcionando executando os testes no terminal, repare que não precisamos escrever um teste se quer, pois
faremos isso em seguida.

    cd mysite/polls/
    python manage.py test polls --testrunner=mysite.settings_noDB.TestRunnerWithoutDB

E o resultado é...

    ----------------------------------------------------------------------
    Ran 0 tests in 0.000s

    OK

Vou quebrar a linha de comando para entendermos melhor.

    python manage.py test polls     # até aqui nada de novo
    --testrunner=                   # aqui vamos dizer quem será o executor de testes (test runner)
        mysite                      # esse é nome do seu projeto
            .settgins_noDB          # esse é o nome do arquivo de configuração
            .TestRunnerWithoutDB    # esse é o nome da classe

Agora basta escrever os testes, este é um passo importante pois não utilizaremos mais a classe `TestCase` e sim a classe
`SimpleTestCase` que, segundo a documentação, é um atalho para __unittest__. Veja exemplo...

```python
from django.test import SimpleTestCase

class ExampleUnitTest(SimpleTestCase):
    def test_foo(self):

        # importar alguma coisa
        # from . import *

        #
        # fazer alguma coisa
        #
        def foo():
            return 1

        # testar...
        self.assertEqual(1, foo())
```



