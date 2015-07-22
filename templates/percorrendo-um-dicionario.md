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

Utilizando a função forloop() para enumerar cada item

```python
{% for key, value in checkboxes.items %}
    <input type="checkbox" id='check{{forloop.counter}}' name="check" value='{{forloop.counter}}'>
    <label for="check{{forloop.counter}}">{{ value }}</label><br>
{% endfor %}
```

O resultado do código html ficaria assim...

```html
<input id="check1" name="check" value="1" type="checkbox">
<label for="check1">primeira frase</label><br/>
<input id="check2" name="check" value="2" type="checkbox">
<label for="check2">segunda frase</label><br/>
...
```