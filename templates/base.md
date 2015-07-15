Template Base
===

Um exemplo de como utilizar o sistema de template do Django.

Considere a seguinte estrutura.

    project/
        app/
            templates/
                base.html
                pagina.html

Abaixo teremos o arquivo `base.html`.

```html
<!DOCTYPE html>
<html lang="pt-br">
    <head>
        <title>Template</title>
        <meta charset="UTF-8">
    </head>
    <body>

        {% block conteudo %}{% endblock %}

    </body>
</html>
```

Abaixo teremos o arquivo `pagina.html`.

```html
{% extends 'template_html/base.html' %}

{% block conteudo %}

    <h1>Título</h1>
    
    <p>Parágrafo</p>
    <p>Parágrafo</p>
    <p>Parágrafo</p>
    
{% endblock conteudo %}
```

