Namespaces
===

Se, nos templates, quisermos referenciar funções com o mesmo nome, como por exemplo `index`, deveremos utilizar os 
__namespaces__ para que não haja conflitos.

```html
<a href="{% url 'index' %}">Index</a><br/>
<a href="{% url 'app1:index' %}">Aplicação - 1</a><br/>
<a href="{% url 'app2:index' %}">Aplicação - 2</a><br/>
```

Conforme o exemplo, no arquivo `urls.py` do app1 temos a URL `index`: 

    url(r'^$', views.index, name='index'),

E na app2 temos o mesmo nome `index` na URL:

    url(r'^$', views.index, name='index'),

Isso gera um conflito porque o Django não sabe para qual index o link está fazendo a requisição.

Para o Django descobrir qual a URL correta devemos definir no arquivo `urls.py` do projetoc um namespace para cada 
aplicação.

    url(r'^app1/$', include('app1.urls', namespace='app1')),
    url(r'^app2/$', include('app2.urls', namespace='app2')),

Lembrando que o namespace só funciona em URLs que contém o atributo `name` já definido em cada URL, ele __não funciona__
ao chamar a view diretamente, como no exemplo abaixo:

    <a href="{% url 'app1:views.index' %}">App 1</a><br/>

Porém, ele funcionaria na forma básica (sem utilização de namespaces):

    <a href="{% url 'app1.views.index' %}">App 1</a><br/>

Obs.:

Ao utilizar o redirect é necessário também colocar o seu namespace ao requisitar a view.

    redirect('app1:views.index')