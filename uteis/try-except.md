Tratando erros (Try Except)
===

[https://docs.djangoproject.com/en/1.8/ref/exceptions/](https://docs.djangoproject.com/en/1.8/ref/exceptions/)
[https://docs.python.org/3/library/exceptions.html#built-in-exceptions](https://docs.python.org/3/library/exceptions.html#built-in-exceptions)

Como é o try execption????

```python
from django.shortcuts import render,redirect

def index(request):
    try:
        1/0
    
    except Exception as e:
        print(e)
```

No exemplo abaixo é mostrado como utilizar o tratamento de erros ao utilizar uma SESSION. O erro ocorre quando o usuário 
tenta recuperar a SESSION exemplo, mas não o encontra no sistema, causado o erro `KeyError`.

```python
from django.shortcuts import render,redirect

def index(request):
    try:
        print(request.session['foo'])
    
    except KeyError as e:
        print(e)
```

Abaixo um exemplo de como tratar o erro do Paginator do Django.

```python
try:
    # Retorna a paginação
    posts = paginator.page(page)

except PageNotAnInteger:
    # Abriremos qual página quando não encontrar um número inteiro
    posts = paginator.page(1)

except EmptyPage:
    # Se a quantidade da itens por página for menor que o limite máximo de itens, retorna o número 1.
    posts = paginator.page(paginator.num_pages)
```