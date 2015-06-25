Enviando o contexto para o Template
===

[https://docs.djangoproject.com/en/1.8/ref/templates/api/#rendering-a-context](https://docs.djangoproject.com/en/1.8/ref/templates/api/#rendering-a-context)

[https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#render](https://docs.djangoproject.com/en/1.8/topics/http/shortcuts/#render)


No Django 1.8 o argumento `context` passou a se chamar `dictionary`.

O argumento `dictionary` pode ser enviado para o template de duas formas:

A forma mais simples de se enviar um contexto para o template, é quando se tem apenas uma chave no `dictionary`:

    foo['texto'] = 'Uma string qualquer...'

Neste caso o `dictionary` é enviado apenas como variável simples para o template.

    return render (request, 'template/index.html', foo)

Para renderizar o contexto enviado para o template, utiliza a chave do `dictionary`, ao invés do nome da variável:

    <p>{{teste}}</p>

O resultado seria...

    <p>Uma string qualquer...</p>

A forma mais comum de se enviar um contexto, é quando se tem mais de uma chave no `dictionary`:

    foo['texto']  = 'Uma string qualquer...'
    foo['numero'] = 1234567890
    foo['qualquer-nome']    = '...'

Neste caso o `dictionary` será enviado como uma lista para o template.

    return render (request, 'template/index.html', {'foo2': foo})

Para renderizar o contexto enviado para o template, utiliza o nome da variável seguido pelo nome da chave.

    <p>{{foo2.texto}}</p>
    <p>{{foo2.numero}}</p>
    <p>{{foo2.qualquer-nome}}</p>

O resultado seria...

    <p>Uma string qualquer...</p>
    <p>1234567890</p>
    <p>...</p>