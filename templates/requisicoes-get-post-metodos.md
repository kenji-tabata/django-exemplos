Métodos de requisição para GET e POST 
===

[https://docs.djangoproject.com/en/1.8/ref/request-response/#querydict-objects](https://docs.djangoproject.com/en/1.8/ref/request-response/#querydict-objects)

Todas as requisições GET e POST são tratados como um dicionário pelo Django, ou seja, ao enviar um formulário de contato 
por exemplo, os dados preenchidos deste formulário será enviado como parte do dicionário do objeto `request`. 
Isso possibilita interagir facilmente com os dados do objeto `request` com as suas funções disponíveis.

Os métodos abaixo funcionam tanto para o GET quanto para o POST.

```python
# Retorna o valor da `key` escolhido, caso não encontre retorna `''`
request.POST.__getitem__('key')

# Retorna `True` caso a `key` existir, caso contrário retorna `False`
request.POST.__contains__('key')

# Retorna o valor da `key`, caso não encontre retorna `none` ou o valor escolhido
request.POST.get('key', 'value')
# O método é utilizado quando 
# o atributo do `model` recebe o valor do checkbox ou do combobox,
# assim podemos definir qual o valor padrão quando o usuário não seleciona uma opção.

# Retorna a `key` e `value` de todos os atributos (iterable)
request.POST.items()

# Retorna apenas o `value` de todos os atributos (iterable)
request.POST.values()

# Retorna sempre uma lista com o `value` da `key`, caso não encontre retorna [] ou o valor escolhido
request.POST.getlist('key','value')
# O método é utilizado quando 
# o atributo do `model` recebe o valor do checkbox ou do combobox com múltiplos valores,
# assim podemos definir qual o valor padrão quando o usuário não seleciona uma opção.

# Retorna os dados da requisição em formato de dicionário
request.POST.dict()
```