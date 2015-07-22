Criando um formulário simples
===

Criando, salvando e visualizando os dados de um textbox

Arquivo do `models.py` adicione as linhas abaixo...

```python
# mysite/textbox/models.py
from django.db import models
from django.utils import timezone

class Postagem(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateTimeField('Publicado', default=timezone.now)
    email = models.EmailField('E-mail', max_length=250)
    url = models.URLField('Site')
    rating = models.DecimalField(max_digits=9, decimal_places=1)
    like = models.IntegerField()
    conteudo = models.TextField('Conteúdo')
    
    def __str__(self):
        return self.titulo
```

Na view adicione as funções `index` para renderizar o formulário, o `enviar` para inserir o registro e 
o `listar` para visualizar os itens como lista.


```python
# mysite/textbox/views.py
from django.shortcuts import render, redirect
from app.models import Post

def index(request):
    return render(request, 'textbox/index.html', {})

def listar(request):
    listar_posts = Post.objects.order_by('-data')
    return render(request, 'textbox/listar.html', {'listar_posts':listar_posts})

def enviar(request):
    if request.method == 'POST':
        postagem = Postagems.objects.create(
            titulo = request.POST['titulo'],
            email = request.POST['email'],
            url = request.POST['url'],
            rating = request.POST['rating'],
            like = request.POST['like'],
            conteudo = request.POST['conteudo'],
        )
        
        return redirect('textbox.views.listar')
    
    return render(request, 'app/index.html', {})
```

No arquivo `urls.py` adicione as linhas abaixo...

```python
# mysite/textbox/urls.py
from django.conf.urls import patterns, url
from textbox import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)
```

E por último criamos os templates das páginas `index` para exibir o formulário...

```html
<!-- mysite/textbox/templates/index.html -->
<form action="{% url 'enviar' %}" method="POST">
    {% csrf_token %}
    <label for='titulo'>Título: </label><br>
    <input type='text' id='titulo' name='titulo' placeholder="Titulo"/><br>
    <label for='email'>E-mail: </label><br>
    <input type='email' id='email' name='email' placeholder="E-mail"/><br>
    <label for='url'>Site: </label><br>
    <input type='url' id='url' name='url' placeholder="Site"/><br>
    <label for='rating'>Pontuação: </label><br>
    <input type='number' id='rating' name='rating' placeholder="Pontuação"/><br>
    <label for='like'>Like: </label><br>
    <input type='number' id='like' name='like' placeholder="0"/><br>
    <label for='conteudo'>Conteúdo: </label><br>
    <textarea id='conteudo' name='conteudo' placeholder="Insira o texto aqui..."></textarea><br>
    <input type="submit" id='enviar' name='enviar' value='Enviar'><br>
</form>
```

E para listar todos os registros.

```html
<!-- mysite/textbox/templates/listar.html -->
{% if listar_posts %}
    {% for post in listar_posts %}
        <b>Título: </b> {{ post.titulo }}<br>
        <b>Data: </b> {{post.data}}<br>
        <b>E-mail </b> {{ post.email }}<br>
        <b>Site: </b> {{post.url}}<br>
        <b>Pontuação: </b> {{ post.rating }}<br>
        <b>Like: </b> {{post.like}}<br>
        <b>Conteúdo: </b> {{post.conteudo}}<br><br>
    {% empty %}
        <p>Nenhum post foi encontrado</p>
    {% endfor %}
{% endif %}

<a href="{% url 'index' %}">Voltar</a>
```

