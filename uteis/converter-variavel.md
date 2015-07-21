Converter variável...
===

String para Array, separado por vírgula
---

### Exemplo 1:

Entrada = "['carro','moto']"
Saída   = ['carro','moto']

```python
import re

def converter_string_list(str):
    rm_caracter = re.sub("[^A-Za-z0-9Á-Źá-ź,-_+*.]", '', str)
    return rm_caracter.split(',')
```

### Exemplo 2:

Entrada = "Aluga-se casa,Rua Arouche 44,+ 2 Quartos,5*10m,Em construção."
Saída   = ['Aluga-se casa', 'Rua Arouche 44', '+ 2 Quartos', '5*10m', 'Em construção.']

```python
import re

def converter_string_list_frases(str):
    rm_caracter = re.sub("[^A-Za-z0-9Á-Źá-ź,+*.!:@#_$%-&\s]", '', str)
    return rm_caracter.split(',')
```


String para dicionário, separado por vírgula
---

### Exemplo 1:

Entrada: key = "Tipo,Marca,Modelo,Cor,Valor", value = "carro,Fiat,Uno,branco,R$ 25.000"
Saída:   {'Tipo': 'carro', 'Marca': 'Fiat', 'Modelo': 'Uno', 'Cor': 'branco', 'Valor': 'R$ 25.000'}

```python
def converter_string_dict(str_key, str_value):
    k_list = str_key.split(',')
    v_list = str_value.split(',')

    return dict(zip(k_list,v_list))
```

### Exemplo 2:

Entrada: value = "carro,Fiat,Uno,branco,R$ 25.000"
Saída:   {0: 'carro', 1: 'Fiat', 2: 'Uno', 3: 'branco', 4: 'R$ 25.000'}

```python
def converter_string_dict(str_value):
    v_list = str_value.split(',')
    chave  = len(v_list)
    
    array =dict(zip([c for c in range(chave)],[vl[j] for j in range(chave)]))
    
    return array
```

String para array com dicionário, separado por vírgula
---

### Exemplo 1:

Entrada: key = "Tipo,Marca,Modelo,Cor,Valor", value = "carro,Fiat,Uno,branco,R$ 25.000"
Saída:   [{'Tipo': 'carro'}, {'Marca': 'Fiat'}, {'Modelo': 'Uno'}, {'Cor': 'branco'}, {'Valor': 'R$ 25.000'}]

```python
def converter_string_array_dict(str_key, str_value):
    k_list = str_key.split(',')
    v_list = str_value.split(',')
    dic=[]
    
    for indice in range(len(v_list)):
        array = dict(zip([k_list[indice]],[v_list[indice]]))
        dic.append(array)
    
    return dic
```

### Exemplo 2:

Entrada: value = "carro,Fiat,Uno,branco,R$ 25.000"
Saída:   [{1: 'carro'}, {2: 'Fiat'}, {3: 'Uno'}, {4: 'branco'}, {5: 'R$ 25.000'}]

```python
def converter_string_array_dict(str_value):
    v_list = str_value.split(',')
    chave  = 1
    dic=[]
    
    for indice in range(len(v_list)):
        array = dict(zip([chave],[v_list[indice]]))
        chave = chave+1
        dic.append(array)
    
    return dic
```




Array para string
---

Entrada = ['carro','moto']
Saída   = 'carro, moto'

def converter_list_string(arr):
    delimitador = ', '
    return delimitador.join(arr)


Dicionário para string
---

Entrada1: [{'Tipo': 'carro', 'Marca': 'Fiat', 'Modelo': 'Uno', 'Cor': 'branco', 'Valor': 'R$ 25.000'}]
Entrada2: [{'Tipo': 'carro'}, {'Marca': 'Fiat'}, {'Modelo': 'Uno'}, {'Cor': 'branco'}, {'Valor': 'R$ 25.000'}]
Saída:    'Tipo: carro, Marca: Fiat, Modelo: Uno, Cor: branco, Valor: R$ 25.000'

def converter_dict_string(dict):
    texto = str(dict)
    return re.sub("[^A-Za-z0-9Á-Źá-ź,+*.!:@#_$%-&\s]", '', texto)
