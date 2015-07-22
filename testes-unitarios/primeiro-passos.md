Primeiro passos com testes
===

Vamos realizar testes do `models.py` com o Django TestCase.

[https://docs.djangoproject.com/en/1.8/topics/testing/overview/#module-django.test](https://docs.djangoproject.com/en/1.8/topics/testing/overview/#module-django.test)

Para realizar os testes do model utilizamos o arquivo `tests.py` da aplicação, assim o Django irá criar um banco de 
dados temporário para realizar todos os testes. Todos os testes são executados apenas neste banco de dados temporário.

Primeiro criamos a classe de testes...

```python
from django.test import TestCase
from exemplo.models import Usuario

class UsuarioTest(TestCase):
    pass
```

Dentro da classe definimos os parâmetros do objeto com o setUp...

```python
def setUp(self):
    self.usuario = {
        'id': 1,
        'nome': 'Marcos',
        'email': 'marcos@emailcom.br',
    }
```

Podemos definir também vários objetos diferentes do mesmo model...

```python
def setUp(self):
    self.usuario1 = {
        'id': 1,
        'nome': 'Marcos',
        'email': 'marcos@email.com.br',
    }
    self.usuario2 = {
        'id': 2,
        'nome': 'Vanessa',
        'email': 'vanessa@email.com.br',
    }
```

Adicionamos a função para inserir um objeto...

```python
def test_inserir_usuario(self):
    usuario = Usuario.objects.create(**self.usuario)

    self.assertEqual(usuario.id, 1)
```

Para executar o teste utilize no terminal o comando abaixo:

     python manage.py test usuarios


Outra forma de configuração do `setUp` é criando os objetos diretamente ao invés de passar apenas os parâmetros, como 
no exemplo a seguir.

```python
def setUp(self):
    Animal.objects.create(name="Leão", sound="roar")
    Animal.objects.create(name="Gato", sound="miau")
```

Assim podemos recuperar o objeto sem ter que criar o mesmo no teste por exemplo.

```python
def test_som_animais(self):
    leao = Animal.objects.get(name="Leão")
    gato = Animal.objects.get(name="Gato")

    self.assertEqual(leao.som(), 'O Leão faz "roar"')
    self.assertEqual(gato.som(), 'O Gato faz "miau"')
```