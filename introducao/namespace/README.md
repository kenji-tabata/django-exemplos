Namespace
===

O namespace é utilizando para evitar conflitos de URL caso possuem o mesmo nome.

Por exemplo, no arquivo `urls.py` do app01 temos a URL `index`: 

    url(r'^$', views.index, name='index'),

E na app02 temos o mesmo nome `index` na URL:

    url(r'^$', views.index, name='index'),

Isso gera um conflito porque o Django não sabe para qual index o link está fazendo a requisição.

Para o Django enxergar para qual o index ele deve redirecionar ao clicar no link é definido para cada aplicação um namespace,
que é definido no arquivo `urls.py` do projeto.

    url(r'^app01/$', include('app01.urls', namespace='app01')),
    url(r'^app02/$', include('app02.urls', namespace='app02')),

Ao definir o namespace da aplicação, basta adicionar no template o namespace da aplicação ao chamar a URL, como no exemplo 
abaixo:

    <a href="{% url 'app01:index' %}">App 01</a><br/>

Lembrando que o namespace só funciona em URLs que contém o atributo `name` já definido em cada URL, ele não funciona ao 
chamar a VIEW diretamente, como no exemplo abaixo:

    <a href="{% url 'app01:views.index' %}">App 01</a><br/>