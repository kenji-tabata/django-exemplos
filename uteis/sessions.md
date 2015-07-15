Sessions
===

Para utilizar as Session no Django é preciso ter a base de dados devidamente criada, pois ele grava as sessions no banco.
Tenha a certeza de ter executado `python manage.py migrate` ao menos uma vez.

Criando...

```python
request.session['foo'] = "bar"
```

Utilizando assim...

```python
if request.session.__contains__('foo'):
    print(request.session['foo'])
```

Ou assim...

```python
if 'foo' in request.session:
    print(request.session['foo'])
```


Deletando...

```python
del request.session['foo']
```