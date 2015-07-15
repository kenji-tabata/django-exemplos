Criando template de forma dinâmica
===

Se precisar criar um template de forma dinâmica (na memória) podemos fazer como demonstrado abaixo.

```python
from django.shortcuts import render
from django.template import Context, Template


def index(request):
    
    # Criamos um template na memória
    template = Template('<p>Olá {{nome}}!</p>')

    # Criamos o contexto
    context = Context({'nome': 'Fulano'})
    
    # Renderizamos o template
    trecho_html = template.render(context)
        
    return render(request, 'view_html_code/index.html', {'trecho_html': trecho_html})
```

O template principal seria...

```html
<!DOCTYPE html>
<html>
    <head>
        <title></title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
    </head>
    <body>
        
        {{ trecho_html }}
        
    </body>
</html>
```

Será muito útil na criação do controle `select` (combobox).