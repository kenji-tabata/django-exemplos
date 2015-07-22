Métodos para salvar um registro do formulário
===

Quatro maneiras de salvar um registro no banco de dados.

Quando utilizar múltiplos banco de dados adicionar o parâmetro `using='nome-da-conexao'`, 
como no exemplo abaixo:

```python
Posts.objects.using('nome-da-conexao').create()
```

```python
...
posts(using='nome-da-conexao')
```


Com Django ORM
---

```python
posts = Posts.objects.create( titulo = request.POST['titulo'], conteudo = request.POST['conteudo'] )
```


Como objeto
---

```python
posts = Posts()
posts.titulo = request.POST['titulo']
posts.conteudo = request.POST['conteudo']
posts.save()
```

Utilizando o forms para validar (método um)
---

```python
form = NomeDaClasseForm(request.POST)
if form.is_valid():
    form_valid = form.save(commit=False)
    form_valid.data(timezone.now) # Adicione outros atributos que não são enviados pelo formulário
    form_valid.save()
```

Utilizando o forms para validar (método dois)
---

```python
dados = {'titulo': request.POST['titulo'], 'conteudo': request.POST['conteudo']}
form = NomeDaClasseForm(dados)

if form.is_valid():
    form_valid = form.save(commit=False)
    form_valid.data(timezone.now) # Adicione outros atributos que não são enviados pelo formulário
    form_valid.save()
```


Utilizando forms para validar (método três)
---

```python
dados = {'titulo': request.POST['titulo'], 'conteudo': request.POST['conteudo']}
form = NomeDaClasseForm(dados)

if form.is_valid():
    post = Main()
    post.titulo = form.cleaned_data['status']
    post.conteudo = form.cleaned_data['nome']
    post.save()
```
