Requisições: Métodos do GET e POST
===

[https://docs.djangoproject.com/en/1.8/ref/request-response/#querydict-objects](https://docs.djangoproject.com/en/1.8/ref/request-response/#querydict-objects)

Todas as requisições GET e POST são tratados como um dicionário pelo Django, ou seja, ao enviar um formulário de contato 
por exemplo, os dados preenchidos deste formulário será enviado como parte do dicionário do objeto `request`. Isso 
possibilita interagir facilmente com os dados do objeto `request` com as suas funções disponíveis.

Métodos do request
---

Os métodos abaixo funcionam no GET e no POST

__Retorna o valor da `key` escolhido, caso não encontre retorna ''.__

    request.POST.__getitem__('key')

# Retorna True caso a `key` existir, caso contrário retorna False.

    request.POST.__contains__('key')

# Retorna o valor da `key`, caso não encontre retorna `none` ou o valor escolhido.

    request.POST.get('key', 'value')

# Retorna a `key` e `value` de todos os atributos. Interage com o for.

    request.POST.items()

# Retorna apenas o `value` de todos os atributos. Interage com o for.

    request.POST.values()

# Retorna sempre uma lista com o `value` da `key`, caso não encontre retorna [] ou o valor escolhido.

    request.POST.getlist('key','value')

# Retorna os dados da requisição em formato de dicionário.

    request.POST.dict()


Nota 1: O método `request.POST.get('key', 'value')` é utilizado quando o atributo do `model` recebe o valor do checkbox 
ou do combobox, assim podemos definir qual o valor padrão quando o usuário não seleciona uma opção.

Nota 2: O método `request.POST.getlist('key','value')` é utilizado quando o atributo do `model` recebe o valor do 
checkbox ou do combobox com múltiplos valores, assim podemos definir qual o valor padrão quando o usuário não seleciona 
uma opção.

