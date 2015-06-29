Cross Site Request Forgery protection (CSRF Token)
===

[https://docs.djangoproject.com/en/1.8/ref/csrf/](https://docs.djangoproject.com/en/1.8/ref/csrf/)

Ao enviar qualquer tipo de formulário pelo método POST é obrigatório a utilização do CSRF Token, afim 
de proteger o envio da requisição POST no navegador.

Para ativar o CSRF Token adicione na configuração `MIDDLEWARE_CLASSES` do arquivo `settings.py` a linha abaixo:

    MIDDLEWARE_CLASSES = (
        ...
        django.middleware.csrf.CsrfViewMiddleware
    )

Existem ? métodos para se utilizar o CSRF Token.

1. No formulário do Template HTML

```python
<form action="." method="POST">
    {% csrf_token %}
    ...

</form>
```


2. Em uma função especifica da View que utiliza dados enviados por POST

```python
from django.shortcuts import render_to_response
from django.template.context_processors import csrf

def my_view(request):
    c = {}
    c.update(csrf(request))
    # ... view code here
    return render_to_response("a_template.html", c)
```

3. Ao criar um arquivo de configuração `post-csrf.js` para todas as requisições AJAX por POST.

```javascript
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
            // Only send the token to relative URLs i.e. locally.
            xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        }
    }
});
```


    

    