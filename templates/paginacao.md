Paginação
===

Neste exemplo é mostrado como criar um sistema de paginação de maneira simples e funcional no Django.

[Saiba mais](https://docs.djangoproject.com/en/1.8/topics/pagination/)


```python
from django.shortcuts import render_to_response
from paginacao.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):

    # Vamos retornar 500 posts, por exemplo.
    post_list = Post.objects.order_by('id')
    
    # Vou paginar de 100 em 100
    paginator = Paginator(post_list, 100)
    
    # Recebe o número da página pelo link
    page = request.GET.get('page')
    
    try:
        # Retorna a paginação
        posts = paginator.page(page)

    except PageNotAnInteger:
        # Abriremos qual página
        posts = paginator.page(1)

    except EmptyPage:
        # Se a quantidade da itens por página for menor que o limite máximo de itens, retorna o número 1.
        posts = paginator.page(paginator.num_pages)
        
    return render_to_response('paginacao/index.html', {'posts': posts})
```

Nosso template seria semelhante ao exibido abaixo...

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Paginação Django</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        <h1>Posts</h1>
        {% for post in posts %}
            {{ post.titulo|upper }}<br>
            {{ post.conteudo }}<br><br>
        {% endfor %}
        <br>
        <div class="pagination">
            <span class="step-links">
                {% if posts.has_previous %}
                    <a href="?page={{ posts.previous_page_number }}">Anterior</a>
                {% endif %}

                <span class="current">
                    Pagina {{ posts.number }} de {{ posts.paginator.num_pages }}.
                </span>

                {% if posts.has_next %}
                    <a href="?page={{ posts.next_page_number }}">Próximo</a>
                {% endif %}
            </span>
        </div>
        <br>
        <div class="pagination">
            <span class="step-links">
                {% if posts.has_previous %}
                    <a href="?page={{ posts.previous_page_number }}"><<</a>
                {% endif %}

                <span class="current">
                    {% for page in posts.paginator.page_range %}
                        {% if page == posts.number %}
                            {{page}}
                        {% else %}
                            <a href="?page={{ page }}">{{page}}</a>
                        {% endif %}
                    {% endfor %}
                </span>

                {% if posts.has_next %}
                    <a href="?page={{ posts.next_page_number }}">>></a>
                {% endif %}
            </span>
        </div>
    </body>
</html>
```
