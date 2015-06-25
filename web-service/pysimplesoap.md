pysimplesoap + Django
===

Se pretende criar um web service então terá que escolher uma biblio para fazer o meio de campo, neste exemplo estou
utilizando a biblio __pysimplesoap__.

Repositório inicial do projeto https://code.google.com/p/pysimplesoap/

A versão mais atual é a do github https://github.com/pysimplesoap/pysimplesoap

A instalação é simples:

    pip install pysimplesoap

Obs: Eu utilizei Python 3.4. e Django 1.8

Crie uma visão no Django, ela será a nossa versão de servidor.

```python
""" views.py """
from pysimplesoap.server import SoapDispatcher
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

#
# Sua função
#
def adder(a,b):
    "Add two values "
    return a+b

#
# Definindo o dispatcher
#
dispatcher = SoapDispatcher(
    'my_dispatcher',
    location = "http://localhost:8000",
    action = "http://localhost:8000",
    namespace = "http://localhost:8000", 
    prefix="prefix-foo",
    ns = "ns-foo")

#
# Registrando sua função
#
dispatcher.register_function('Adder', adder,
    returns={'AddResult': int}, 
    args={'a': int,'b': int})

#
# Aqui é a view (propriamente dita)
#
@csrf_exempt
def dispatcher_handler(request):
    if request.method == "POST":
        response = HttpResponse(dispatcher.dispatch(request.body))
    else:
        response = HttpResponse(dispatcher.wsdl(), content_type="application/xml")
        # Obs: sem a definição do content-type o retorno será um HTML simples (text/plan)
        # aí já viu né? Vai dar pau!

    response['Content-length'] = str(len(response.content))
    return response
```

Não se esqueça do arquivo `urls.py`

```python
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', '[nome-do-seu-projeto].views.dispatcher_handler', name='home'),
]
```



## Testando (visualmente)

Você executa o servidor embutido (`python manage.py runserver`) e cnfere o  resultado
no seu navegador [http://localhost:8000/](http://localhost:8000/)

Ou você poderá checar via terminal criando um cliente. Crie o arquivo abaixo dentro de sua pasta do projeto 
(qualquer pasta dentro do projeto) e execute no terminal `python cliente.py`

```python
""" client.py """
from pysimplesoap.client import SoapClient, SoapFault

#
# Criando o cliente
#
client = SoapClient(
    location = "http://localhost:8000/",
    action = 'http://localhost:8000/', # SOAPAction
    namespace = "http://example.com/sample.wsdl"
)

#
# Consumindo o web service
#
response = client.Adder(a=1, b=2)

#
# Visualizanbdo o resultado
#
result = response.AddResult
print(int(result))
```



## Bug na biblioteca

Quando acessamos o serviço via terminal obtemos o segunite erro

    VersionMismatch.TypeError: can't use a string pattern on a bytes-like object

Segundo a discução em https://code.google.com/p/pysimplesoap/issues/detail?id=142#c4
a solução encontrada foi alterar __linha 163__ do arquivo 
`[??????]/site-packages/pysimplesoap/server.py` da biliboteca.

Bug...

            ...
            ns = NS_RX.findall(xml)
            ...            

Corrigido...

            ...
            ns = NS_RX.findall(xml.decode("utf-8"))
            ...            

A questão é saber onde está instalada a biblioteca.

