Exemplos práticos AJAX dos eventos Ajax com o Django
===

Ordenando uma lista de uma tabela como ascendente, decrescente e último inserido
---

Adicione `views.py` a função `ordenar_pelo_cabecalho`

```python
from django.shortcuts import render
from lista_filtro.models import Usuario
from django.template import Context, Template

def ordenar_pelo_cabecalho(link, ordem, tipo):
    titulos = ('id', 'nome', 'email', 'data', 'status')
    
    tabHeader =''
    
    for titulo in titulos:
        # Verifica se o nome do parâmetro `tipo` é o mesmo nome do titulo atual, caso seja adiciona o tipo da ordenação.
        if titulo == tipo:
            tabHeader += ("<th><a href='%s' title='%s' id='%s'>%s %s</a></th>" % (link, titulo, titulo, titulo.lower().capitalize(), ordem))
        else:
            tabHeader += ("<th><a href='#asc' title='%s' id='%s'>%s</a></th>" % (titulo, titulo, titulo.lower().capitalize()))
        
    thead = Template(tabHeader)
    
    context = Context({'link': link, 'ordem': ordem})
    
    return thead.render(context)
```

Para ordenar a lista da tabela vamos criar mais quatro funções que irão tratar do envio das requisições.

```python
def index(request):
    list_user = Usuario.objects.all()
    html = ordenar_pelo_cabecalho('#asc', '', '')
    
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

def order_by_asc(request):
    tipo = request.GET.get('tipo')
    html = ordenar_pelo_cabecalho('#desc', 'Asc', tipo)
    
    list_user = Usuario.objects.order_by(tipo)
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

def order_by_desc(request):
    tipo = request.GET.get('tipo')
    html = ordenar_pelo_cabecalho('#', 'Desc', tipo)

    list_user = Usuario.objects.order_by('-'+tipo)
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})
        
def order_by_ult(request):
    list_user = Usuario.objects.order_by('-id')
    html = ordenar_pelo_cabecalho('#', '', '')
    
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})
```

No arquivo `urls.py` adicione as URLs de cada requisição

```python
from django.conf.urls import patterns, url
from lista_filtro import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ordem_asc/$', views.order_by_asc, name='ordem_asc'),
    url(r'^ordem_desc/$', views.order_by_desc, name='ordem_desc'),
    url(r'^ordem_ult/$', views.order_by_ult, name='ordem_ult'),
)


Adicione o Ajax que irá modificar a tabela a cada clique no nome do cabeçalho.

```javascript
$(function () {
    $("#table_list thead a").click(function () {
        var campo = $(this).attr("href");
        var tipo = $(this).attr("title");
        var tablelist = $("#table_list");
        
        if(campo=="#asc"){
            $.get("ordem_asc/", "tipo="+tipo, function (html) {
                tablelist.remove();
                $('body').append(html); 
            }).fail(function (xhr, textStatus, error) {
                console.log(error);
            });
        }
        else if(campo=="#desc"){
            $.get("ordem_desc/", "tipo="+tipo, function (html) {
                tablelist.remove();
                $('body').append(html);
            }).fail(function (xhr, textStatus, error) {
                console.log(error);
            });
        }
        else if(campo=="#"){
            $.get("ordem_ult/", "tipo="+tipo, function (html) {
                tablelist.remove();
                $('body').append(html);
            }).fail(function (xhr, textStatus, error) {
                console.log(error);
            });
        }
    });
});
```

E por fim crie o template HTML...

```html
{% load staticfiles %}
<!DOCTYPE html>
<html>
    <head>
        <title>Filtros e ordenação</title>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <script type="text/javascript" src="{% static 'js/jquery-1.11.2.min.js' %}"></script>
        <script type="text/javascript" src="{% static 'js/script.js' %}"></script>
        <script type="text/javascript" src="{% static 'js/conf_csrf.js' %}"></script>
    </head>
    <body>
        <table id="table_list">
            <thead>
                <tr>
                    {{html}}
                </tr>
            </thead>
            <tbody>
                {% for usuario in list_user %}
                    <tr>
                        <td style="width: 80px">{{usuario.id}}</td>
                        <td><a href="#">{{usuario.nome}}</a></td>
                        <td>{{usuario.email}}</td>
                        <td>{{usuario.data}}</td>
                        <td>{{usuario.status}}</td>
                    </tr>
                {% endfor %}
            </tbody>
        </table>
    </body>
</html>
```