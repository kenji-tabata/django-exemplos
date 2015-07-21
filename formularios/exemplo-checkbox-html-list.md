Exemplo de como criar vários checkbox e salvar como uma lista
===

Ao invés de cada checkbox ter um atributo no model como no exemplo [anterior](exemplo-checkbox-html-crud.md), 
podemos definir um único atributo no model para salvar todos os valores escolhidos dos checkboxes.

Neste exemplo vamos utilizar o seguinte model:

```python
# mysite/checkbox_multi/models.py
from django.db import models

class Transportes(models.Model):
    alternativas = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return str(self.id)
```

O arquivo `urls.py` se mantém o mesmo do exemplo anterior...

```python
# mysite/checkbox_multi/urls.py
from django.conf.urls import patterns,  url
from checkbox_multi import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^ver-alternativas/(?P<pk>[0-9]+)/$', views.carregar, name='ver-alternativas'),
    url(r'^atualizar/(?P<pk>[0-9]+)/$', views.atualizar, name='atualizar'),
    url(r'^deletar/(?P<pk>[0-9]+)/$', views.deletar, name='deletar'),
)
```

Também não sofre alteração as funções index, listar, carregar e deletar do arquivo `views.py` do exemplo anterior.


Inserindo um item
---

A função `enviar`recebe apenas uma variável do POST com todas as alternativas selecionadas no formato de lista

```python
# mysite/checkbox_multi/views.py
def enviar(request):
    if request.method == 'POST':
        transportes = Transportes.objects.create(
            opcoes_transp = request.POST.getlist('opcoes_transp','Nenhuma opção foi escolhida')
        )
        
    return redirect('checkbox_multi.views.listar')
```

No template modificamos o `name` das checkbox para `opcoes_transp`

```python
<form action="{% url 'enviar' %}" method="POST">
    {% csrf_token %}
    <input type='checkbox' name='opcoes_transp' id='carro' value='Carro'/>
    <label for='carro'>Carro</label><br/>
    <input type='checkbox' name='opcoes_transp' id='moto' value='Moto'/>
    <label for='moto'>Moto</label><br/>
</form> 
```


Listando todos os items
---

A view do listar...

```python
def listar(request):
    transportes = Transportes.objects.order_by('-id')
    return render(request, 'checkbox_multi/listar.html', {'transportes':transportes})
```

No template `listar.html` adicionamos um if em cada alternativa que verifica se o `opcoes_transp` tem 
o nome do transporte

```python
{% for transporte in transportes %}
    <p><strong><a href="{% url 'ver-alternativas' transporte.id %}">ID</a>: </strong>{{transporte.id}} / 
        <strong>Carro: </strong>{% if 'Carro' in transporte.opcoes_transp %}Sim {% else %}Não {% endif %} / 
        <strong>Moto: </strong>{% if 'Moto' in transporte.opcoes_transp %}Sim {% else %}Não {% endif %} /
        <strong>Ônibus: </strong>{% if 'Ônibus' in transporte.opcoes_transp %}Sim {% else %}Não {% endif %}/
        <strong>Bicicleta: </strong>{% if 'Bicicleta' in transporte.opcoes_transp %}Sim {% else %}Não {% endif %}| 
        <a href="{% url 'checkbox:deletar' transporte.id %}">Remover</a>
    </p>
{% empty %}
    <p>Nenhuma resposta foi encontrada</p>
{% endfor %}
```


Atualizando um item
---

A função `carregar` da `view.py` se mantém o mesmo como no exemplo anterior...


def carregar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    return render(request, 'checkbox_multi/ver-alternativas.html', {'transporte': transporte})


E o atualizar recebe agora apenas uma váriavel do POST...

def atualizar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    if request.method == 'POST':
        opcoes_transp = request.POST.getlist('opcoes_transp','Nenhuma opção foi escolhida')
                
        transporte.opcoes_transp = opcoes_transp
        transporte.save()
        
    return render(request, 'checkbox_multi/ver-alternativas.html', {'transporte': transporte})
        

No template html somente o if que é alterado conforme o exemplo abaixo

```python
<form action="{% url 'checkbox_multi:atualizar' transporte.id %}" method="POST">
    {% csrf_token %}
    <input type='hidden' name='id' id='{{transporte.id}}' value='{{ transporte.id }}'/>
    <input type='checkbox' name='carro' id='carro' value='Sim' {% if 'Carro' in transporte.carro %} checked {% endif %}/>
    <label for='carro'>Carro</label><br/>
    <input type='checkbox' name='moto' id='moto' value='Sim' {% if 'Moto' in transporte.opcoes_transp %} checked {% endif %}/>
    <label for='moto'>Moto</label><br/>
    <input type="submit" id='enviar' value='Enviar'/><br/>
</form>
```

Removendo um item
---

Se mantém o mesmo do exemplo anterior na `views.py` e no template html.

```html
<p><strong>ID: </strong>{{transporte.id}}
    ...
    <a href="{% url 'deletar' transporte.id %}"> Remover</a>
</p>

```python
def deletar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    transporte.delete()
    
    return redirect('checkbox.views.listar')
```