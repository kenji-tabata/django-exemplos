Requisição Ajax por método POST
===

Os arquivos de JavaScript por padrão devem estar na pasta `static` do projeto, veja em [Arquivos Estáticos](../templates/static-files.md) 
como configurar.

Neste exemplo vamos enviar um formulário POST com o CSRF Token de duas formas, uma para cada requisição POST e a outra 
para todas as requisições POST. Em ambos os casos a `views.py`, `urls.py` e o `index.html` são idênticas.

Primeiro criamos a view que receberá os dados do usuário pelo método POST.

```python
# mysite/polls/views.py
from django.shortcuts import render, redirect
from exemplo.models import Usuario

def enviar(request):
    if request.method == 'POST':
        usuario = Usuario.objects.create(
            nome = request.POST['nome'],
            email = request.POST['email']
        )

    return render(request, 'exemplo/index.html', {})
```

Definimos a URL no arquivo `urls.py`...

```python
# mysite/polls/urls.py
from django.conf.urls import patterns, include, url
from exemplo import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)

E criamos o template...

```html
{% load staticfiles %}
<!DOCTYPE html>
<html>
    <head>
        <title>Exemplo</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script type="text/javascript" src="{% static 'js/jquery-1.11.2.min.js' %}"></script>
        <script type="text/javascript" src="{% static 'js/csrf-conf.js' %}"></script>
        <script type="text/javascript" src="{% static 'js/script.js' %}"></script>
    </head>
    <body>
        <form action="{% url 'enviar' %}" name="formulario" id="formulario" method="POST">
            {% csrf_token %}
            <input type="hidden" name="csrfmiddlewaretoken">
            <p><label for="id_nome">Nome:</label> <input id="id_nome" maxlength="200" name="nome" type="text"></p>
            <p><label for="id_email">Email:</label> <input id="id_email" maxlength="150" name="email" type="email"></p>
            <input type="submit" value="Enviar" id="enviar"/>
        </form>
    </body>
</html>
```

Repare que no template HTML adicionamos um arquivo de JavaScript a mais, esse arquivo irá conter uma configuração de 
envio do CSRF Token explicado no segundo método. 

O primeiro método é utilizado ao enviar o CSRF Token a cada requisição e consiste em montar a variável `serialize` 
com CSRF Token e os dados do formulário.

```javascript
$(function () {
    $("#formulario").submit(function (event) {
        event.preventDefault();
        
        var csrftoken = $("input[name=csrfmiddlewaretoken]").val();
        var nome = $("input[name=nome]").val();
        var email = $("input[name=email]").val();
        var serialize = "csrfmiddlewaretoken=" + csrftoken + "&nome=" + nome + "&email=" + email;

        $.post("/enviar/", serialize, function (html) {
            // Executa uma ação
        }).fail(function (xhr, textStatus, error) {
            alert(error);
        });
    });
});
```

O segundo método consiste em enviar o CSRF Token em todas as requisições POST sem a necessidade de montar a variável 
`serialize`, para isso crie um arquivo de configuração AJAX com o seguinte código:

```javascript
// static/csrf-conf.js
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

E por fim no arquivo `script.js` remova as variáveis e altere o `serialize` para `$(this).serialize()`.

```javascript
// static/script.js
$(function () {
    $("#formulario").submit(function (event) {
        event.preventDefault();
        $.post("/enviar/", $(this).serialize(), function (html) {
            // Executa uma ação
        }).fail(function (xhr, textStatus, error) {
            alert(error);
        });
    });
});
```