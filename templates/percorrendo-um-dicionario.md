Percorrendo um dicionário
===

Definindo na `views.py`

```python
from django.shortcuts import render

def index(request):
    dados = {'key1': "Reposta 01", 'key2': "Reposta 02", 'key3': "Reposta 03", 'key4': "Reposta 04"}
    
    return render(request, 'array_list/index.html', {'dados': dados})
```

Renderizando no template HTML

```python
{% for key, value in dados.items %}
    <p>Key: {{ key }}, Valor: {{ value }}<p>
{% endfor %}
```