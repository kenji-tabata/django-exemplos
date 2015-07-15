Criando o seu próprio sistema de login auxiliado por classes
===

Para não misturar na view as requisições com o processo de login do Django, podemos separar essa 
funcionalidade em uma classe separada e realizar os testes das funções de forma mais concreta.


Iniciamos criando a classe `LoginUsuario` que conterá a função para autenticar o usuário.

```python
# mysite/polls/login_usuario.py
from django.contrib.auth import authenticate, login

class LoginUsuario(object):
    def autenticar_usuario (self, request, usuario, senha):

        # Função do Django que autentica o usuário
        user = authenticate(username=usuario, password=senha)

        if user is not None:
            if user.is_active:
                login(request, user)
                return True
            else:
                return 'desativado'
        else:
            return False
```

Adicione no arquivo `urls.py` as seguites urls abaixo:

- a url no qual o usuário será redirecionado quando efetuar o login,
- a url que irá renderizar o formulário de login,
- a url que irá enviar o usuário e senha para efetuar o login e
- a url para sair do sistema


```python
# mysite/polls/urls.py
from django.conf.urls import url

from polls import views

urlpatterns = [

    # Index
    url(r'^$', views.index, name='index'),
    
    # Formulário de login
    url(r'^login/$', views.view_login, name='login'),
    
    # Envia o formulário de login
    url(r'^acessar/$', views.acessar, name='acessar'),

    # Sai do sistema
    url(r'^sair/$', views.sair, name='sair'),
]
```

Na view adicionamos apenas as funções para fazer requisições do template para o index, 
login, acessar e sair. 

Vale lembrar que é preciso importar a classe `LoginUsuario` para a função `autenticar_usuario` 
funcionar.

```python
# mysite/polls/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Importando a classe login_usuario
from polls.usuario import LoginUsuario


@login_required(login_url='/login')
def index(request):
    return render(request, 'polls/index.html', {})

def view_login(request):
    return render(request, 'polls/login.html', {})

def acessar(request):
    usuario = senha = ''
    estado = "Digite seu Nome de usuário e senha."

    # Crie o objeto LoginUsuario para acessar suas funções
    login_usuario = LoginUsuario()

    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')

        # O `autorizado` recebe o resultado da função do login
        autorizado = login_usuario.autenticar_usuario(request, usuario, senha)

        if autorizado == True:
            # Redireciona para a página de usuário logado
            return redirect('polls.views.index')

        # Modifica o status pelas mensagens de erro.
        elif (autorizado == 'desativado'):
            status = 'O login deste usuário está desativado.'
        else:
            status = 'O usuário ou senha está incorreto.'
   
    return render(request, 'polls/login.html', {'status': status, 'username': usuario})

def sair(request):
    logout(request)
    return redirect('polls.views.view_login')
```

Repare que ao adicionar o decorador `login_required` acima da função `index` ele bloqueia o acesso a página 
`index.html` quando o usuário não estiver logado.

Veja mais sobre o [`login_required`](https://docs.djangoproject.com/en/1.8/topics/auth/default/#the-login-required-decorator)

No template que responde pelo login (`mysite/polls/login.html`) adicionamos o formulário de login. 

```python
{# Exibe as mensagens de erro do login #}
{% if status %}
    {{status}}
{% endif %}

<form method="POST" action="{% url 'acessar' %}">
    {% csrf_token %}

    {% if next %}
        <input type="hidden" name="next" value="{{ next }}" />
    {% endif %}

    <label for='usuario'>Usuário: </label>
    <input type="text" name="username" id="usuario" value="{{ username }}" /><br />
    <label for="senha">Senha: </label>
    <input type="password" name="password" id="senha" value="" /><br />

    <input type="submit" value="Acessar" />
</form>
```


No template index (`mysite/polls/index.html`) adicione o conteúdo quando o usuário estiver logado.

```python
{% if user.is_authenticated %}
    <p>Bem vindo, {{ user.username }}  <a href="{% url 'logout' %}">[logout]</a></p>
    <p>Área protegida pelo sistema de login do Django.</p>

{% endif %}
```




