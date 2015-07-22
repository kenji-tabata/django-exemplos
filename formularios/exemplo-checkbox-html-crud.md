Exemplo de como criar um checkbox com CRUD em HTML
===

Vamos utilizar o model abaixo para salvar os dados dos checkbox. No caso serão um checkbox para cada alternativa.

```python
# mysite/checkbox/models.py
from django.db import models

class Transportes(models.Model):
    carro     = models.CharField(max_length=3, blank=True, null=True)
    moto      = models.CharField(max_length=3, blank=True, null=True)

    def __str__(self):
        return str(self.id)
```

Inserindo um item
---

No arquivo `views.py` adicionamos primeiro a função para enviar o formulário...

```python
# mysite/checkbox/views.py
from django.shortcuts import render, get_object_or_404, redirect
from checkbox.models import Transportes

def enviar(request):
    if request.method == 'POST':
        
        # A função `request.POST.get()` retorna o valor do checkbox, caso o contrário retorna o valor 'Não'
        p_carro = request.POST.get('carro','Não')
        p_moto = request.POST.get('moto','Não')

        transportes = Transportes.objects.create(
            carro = p_carro,
            moto = p_moto,
        )
            
    return redirect('checkbox.views.listar')
```

No arquivo `urls.py` adicione a url para enviar o formulário...

```python
# mysite/checkbox/urls.py
from django.conf.urls import patterns,  url
from checkbox import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)
```

Por fim crie o template `index.html` com o formulário para enviar as respostas.

```python
<!-- mysite/checkbox/templates/checkbox/index.html-->
<h1>Inserir item</h1>
<form action="{% url 'enviar' %}" method="POST">
    {% csrf_token %}
    <input type='checkbox' name='carro' id='carro' value='Sim'/>
    <label for='carro'>Carro</label><br/>
    <input type='checkbox' name='moto' id='moto' value='Sim'/>
    <label for='moto'>Moto</label><br/>
    <input type="submit" id='enviar' value='Enviar'/><br/>
</form>
```


Listando todos os items
---

Para listar todos os items da tabela `Transportes` adicione na `views.py` a função abaixo...

```python
def listar(request):
    transportes = Transportes.objects.order_by('-id')
    return render(request, 'checkbox/listar.html', {'transportes':transportes})
```

No `urls.py` adicione mais uma url para listar todos os items...

```python
url(r'^listar/$', views.listar, name='listar'),
```

E crie o template para o listar

```html
<!-- mysite/checkbox/templates/checkbox/listar.html-->
<h1>Listando as alternativas</h1>
{% for transporte in transportes %}
    <p><strong>ID: </strong>{{transporte.id}} / 
        <strong>Carro: </strong>{{transporte.carro}} / 
        <strong>Moto: </strong>{{transporte.moto}}
    </p>
{% empty %}
    <p>Nenhuma resposta foi encontrada</p>
{% endfor %}
```


Atualizando um item
---

Para atualizar o item selecionado criamos duas funções na `views.py`, uma para carregar as informações e outra para 
salvar as alterações como no exemplo abaixo...

```python
def carregar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    return render(request, 'checkbox/ver-alternativas.html', {'transporte': transporte})

def atualizar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    if request.method == 'POST':
        p_carro = request.POST.get('carro','Não')
        p_moto = request.POST.get('moto','Não')
                
        transporte.carro = p_carro
        transporte.moto = p_moto
        transporte.save()
        
    return render(request, 'checkbox/ver-alternativas.html', {'transporte': transporte})
```

Adicionamos uma nova url no arquivo `urls.py` para ver as informações

```python
url(r'^ver-alternativas/(?P<pk>[0-9]+)/$', views.carregar, name='ver-alternativas'),
```

E criamos o template para ver as informações.

```html
<!-- mysite/checkbox/templates/checkbox/ver-alternativas.html -->
<p><a href="{% url 'index' %}">Adicionar</a> | <a href="{% url 'listar' %}">Listar</a> | </p>
{% if transporte %}
    <form action="{% url 'atualizar' transporte.id %}" method="POST">
        {% csrf_token %}
        <input type='hidden' name='id' id='{{transporte.id}}' value='{{ transporte.id }}'/>
        <input type='checkbox' name='carro' id='carro' value='Sim' {% if transporte.carro == "Sim" %} checked {% endif %}/>
        <label for='carro'>Carro</label><br/>
        <input type='checkbox' name='moto' id='moto' value='Sim' {% if transporte.moto == "Sim" %} checked {% endif %}/>
        <label for='moto'>Moto</label><br/>
        <input type="submit" id='enviar' value='Enviar'/><br/>
    </form>
{% endif %}
```


Removendo item
---

Para adicionar o link de remover o item adicione no `listar.html` a linha abaixo

```html
<p><strong>ID: </strong>{{transporte.id}}
    ...
    <a href="{% url 'deletar' transporte.id %}"> Remover</a>
</p>

Adicione no arquivo `urls.py` a URL...

```python
url(r'^deletar/(?P<pk>[0-9]+)/$', views.deletar, name='deletar'),
```

E adicione a função `deletar` na `views.py`

```python
def deletar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    transporte.delete()
    
    return redirect('checkbox.views.listar')
```