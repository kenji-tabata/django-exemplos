Criando o seu próprio sistema de login
===

[https://docs.djangoproject.com/en/1.8/topics/auth/default/#how-to-log-a-user-in](https://docs.djangoproject.com/en/1.8/topics/auth/default/#how-to-log-a-user-in)

Podemos criar a nossa própria função de login na `view.py` utilizando os 
módulo `django.contrib.auth` e personalizar a renderização do template


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

Na view importe os módulos e adicione as funções `index`, `login`, `acessar` e `sair`


```python
# mysite/polls/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    return render(request, 'polls/index.html', {})

def view_login(request):
    return render(request, 'polls/login.html', {})

def acessar(request):
    usuario = senha = ''
    estado = "Digite seu Nome de usuário e senha."

    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')

        # Função do Django que autentica o usuário
        user = authenticate(username=usuario, password=senha)

        # Verifica se o usuário existe no banco de dados
        if user is not None:

            # Verifica se o usuário está ativado
            if user.is_active:

                # Função do Django que faz a requisição de login
                login(request, user)

                # Redireciona o usuário para a view `index`
                return redirect('polls.views.index')
            else:
                status = "Usuário não está ativo"

        else:
            status = "Usuário ou senha incorreto"

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