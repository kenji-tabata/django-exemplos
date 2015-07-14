Utilizando arquivos estáticos de outras aplicações
===

Devido a própria natureza das aplicações do Django é possível utilizar um arquivo da pasta `static` em diferentes 
aplicações. Por exemplo, podemos reutilizar uma função de JavaScript da aplicação `polls` na aplicação `app02`, 
evitando assim uma possível duplicação de código.

Exemplo de uma estrutura do projeto

    mysite
    |__ polls
    |   |__ templates
    |   |__ static
    |   |   |__ js
    |   |       |__ polls.js
    |   |
    |__ app_02
    |   |__ templates
    |   |__ static
    |   |   |__ js
    |   |       |__  script02.js
    |   |
    |__ app...
    |   |__ templates
    |   |__ static
    |   |   |__ js
    |   |       |__ script....js
    |   |


Desta forma para a aplicação `polls` iniciar com o seu javascript basta utilizar o caminho abaixo...

```html
<script type="text/javascript" src="{% static 'js/polls.js' %}"></script>
```

Para utilizar um JavaScript de uma outra aplicação basta utilizar o mesmo caminho demonstrado acima...

```html
<script type="text/javascript" src="{% static 'js/script02.js' %}"></script>
```

O Django já identifica para qual aplicação o JavaScript está sendo referenciado.

Isso só é possível quando definimos no arquivo `settings.py` o PATH da pasta `static` de cada aplicação, como no exemplo 
abaixo:

```python
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "polls/static"),
    os.path.join(BASE_DIR, "app02/static"),
    os.path.join(BASE_DIR, "app.../static"), 
)
```

Evite nomear os arquivos `.js` e `.css` com nomes parecidos, como por exemplo `script.js` ou `style.css` em aplicações 
diferentes, evitando assim de sobreescrever os arquivos quando utilizar o comando `python manage.py collectstatic`.