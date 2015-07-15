Exemplo de links
===


A forma mais básica de se criar um link em um template é conhecido como "Hardcoded URL".

    <a href="/enquetes/">Enquetes</a>

Para evitar o Hardcoded podemos utilizar "Template TAG".

    <a href="{% url 'views.enquetes' %}">Enquetes</a>

Para que o código acima funcionar será preciso termos o arquivo `app/urls.py` configurado como abaixo.

```python
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^enquetes$', views.enquetes),
)
```

Podemos simplificar utilizando a propriedade `name`.

```python
urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^enquetes$', views.enquetes, name='enquetes'),
)
```

E o template ficaria como abaixo.

    <a href="{% url 'enquetes' %}">Enquetes</a>

Podemos também recuperar a URL de uma app diferente da atual, por exemplo a função `foo()` da app `blog`.

    <a href="{% url 'blog.views.foo' %}">Foo blog</a>
