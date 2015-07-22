Criando um formulário com o auxilio do forms
===

Criando, salvando e visualizando os dados de um textbox com forms

Arquivo do `models.py` adicione as linhas abaixo...

```python
# mysite/textbox_forms/models.py
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

Adicione a classe `forms.py` que auxilia na validação e na renderização do formulário no template.

```python
# mysite/textbox_forms/forms.py
from django import forms
from textbox_forms.models import Postagem

class PostagensForm(forms.ModelForm):
    
    class Meta:
        model = Postagem
        fields = ('titulo', 'email','url','rating','like','conteudo')
```

Na view adicione as funções `index` para renderizar o formulário, o `enviar` para inserir o registro e 
o `listar` para visualizar os itens como lista.


```python
# mysite/textbox_forms/views.py
from django.shortcuts import render, redirect
from textbox_forms.models import Postagem
from textbox_forms.forms import PostagensForm

def index(request):
    return render(request, 'textbox_forms/index.html', {})

def listar(request):
    listar_posts = Postagem.objects.order_by('-data')
    
    return render(request, 'textbox_forms/listar.html', {'listar_posts':listar_posts})

def enviar(request):
    if request.method == 'POST':
        form = PostagensForm(request.POST)
        if form.is_valid():
            form_valid = form.save(commit=False)
            form_valid.save()
        
        return redirect('textbox_forms.views.listar')
    
    return render(request, 'textbox_forms/index.html', {})
```

No arquivo `urls.py` adicione as linhas abaixo...

```python
# mysite/textbox_forms/urls.py
from django.conf.urls import patterns, url
from textbox_forms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)

```

E por último criamos os templates das páginas `index` para exibir o formulário...

```html
<!-- mysite/textbox_forms/templates/index.html -->
<form action="{% url 'enviar' %}" method="POST">
    {% csrf_token %}
    <label for='titulo'>Título: </label><br>
    <!-- O atributo 'name' de todos os inputs devem ser os mesmos nomes que estão definidos no 'model.py' -->
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
<!-- mysite/textbox_forms/templates/listar.html -->
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

