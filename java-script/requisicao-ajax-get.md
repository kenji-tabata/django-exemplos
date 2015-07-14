Requisição Ajax por método GET
===

Os arquivos de JavaScript por padrão devem estar na pasta `static` do projeto, veja em [Arquivos Estáticos](../templates/static-files.md) 
como configurar.

Primeiro criamos a view que receberá as requisições AJAX pelo método GET, neste exemplo vamos criar uma combobox 
dinâmica.

```python
# mysite/polls/views.py
from django.shortcuts import render
from django.http import HttpResponse

def filtrar_cidade(request):

    # Criamos 3 arrays que armazenará o id e o nome da cidade de cada estado
    mg = [[1, u'Juiz de Fora'], [2, u'Belo Horizonte'], [3, u'Ouro Preto']]
    rj = [[4, u'Rio de Janeiro'], [5, u'Cabo Frio'], [6, u'Búzios']]
    sp = [[7, u'São Paulo'], [8, u'Barueri'], [9, u'Campinas']]

    # Recuperamos o estado escolhido
    estado = request.GET.get('estado')

    html = u'<option value="">Selecione...</option>'

    # Verifica qual o estado selecionado
    if estado == 'MG':
        # Atualiza a variável `html` com os nomes das cidades
        for cidade in mg:
            html = u'{0}<option value="{1}">{2}</option>'.format(html, cidade[0], cidade[1])

    elif estado == 'RJ':
        for cidade in rj:
            html = u'{0}<option value="{1}">{2}</option>'.format(html, cidade[0], cidade[1])

    elif estado == 'SP':
        for cidade in sp:
        html = u'{0}<option value="{1}">{2}</option>'.format(html, cidade[0], cidade[1])

    return HttpResponse(html)
``` 

Depois adicionamos a URL da requisição no arquivo `urls.py`

```python
#mysite/polls/urls.py
from django.conf.urls import url
from exemplo import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^filtrar_cidade/$', views.filtrar_cidade, name='filtrar_cidade'),
]
```

Criamos a função AJAX que enviará as requisições...

```javascript
// static/script.js
$(function () {
    $("#estado").change(function () {
        var estado = $(this).val();
        // A URL deve ser a mesma que está configurada no arquivo `urls.py`
        $.get("filtrar_cidade/", "estado="+estado, function (html){
            $("#cidade").html(html);
        }).fail(function (xhr, textStatus, error) {
            alert(error);
        });
    });
});
```

E por fim criamos o template 

```html
{% load staticfiles %}
<!DOCTYPE html>
<html>
    <head>
        <title>Ajax</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        
        <!-- JQuery -->
        <script type="text/javascript" src="{% static 'js/jquery-1.11.2.min.js' %}"></script>
        
        <script type="text/javascript" src="{% static 'js/script.js' %}"></script>
    </head>
    <body>
        <form>
            <div>
                <label for="estado">Estado</label>
                <select name="estado" id="estado">
                    <option value="">Selecione...</option>
                    <option value="MG">Minas Gerais</option>
                    <option value="RJ">Rio de Janeiro</option>
                    <option value="SP">São Paulo</option>
                </select>
            </div>
            <div>
              <label for="cidade">Cidade</label>
              <select name="cidade" id="cidade">
                <option value="">Selecione...</option>
              </select>
            </div>
        </form>
    </body>
</html>
```


