Utilizando o sistema de login padrão do Django
===

[https://docs.djangoproject.com/en/1.8/topics/auth/default/#using-the-django-authentication-system](https://docs.djangoproject.com/en/1.8/topics/auth/default/#using-the-django-authentication-system)

A forma mais simples de se utilizar o login do Django é utilizando a classe 
`django.contrib.auth.views.login` no template.


Iniciamos configurando o arquivo `settings.py` de forma que o Django saiba para qual página o usuário será redirecionado 
após efetuar o login. No exemplo abaixo definimos o redirecionamento para o `index`.

```python
LOGIN_REDIRECT_URL = '/'
```

Em seguida, no arquivo `urls.py`, devemos definir:

- a url no qual o usuário será redirecionado quando efetuar o login,
- a url que irá renderizar o formulário de login e
- a url para sair do sistema

```python
# mysite/polls/urls.py
from django.conf.urls import url

from polls import views

urlpatterns = [
    
    # Está é a index
    url(r'^$', views.index, name='index'),
    
    # E este é o formulário de login
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login/login.html'}, name='login'),

    # Para sair do sistema
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),
]
```

Em sua view importe o decorator `login_required` e adicione as funções `index` e `login`.

```python
# mysite/polls/view.py
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def index(request):
    return render(request, 'polls/index.html', {})

def login(request):
    return render(request, 'polls/login.html', {})

```

Repare que ao adicionar o decorador `login_required` acima da função `index` ele bloqueia o acesso a página 
`index.html` quando o usuário não estiver logado. 

Veja mais sobre o [`login_required`](https://docs.djangoproject.com/en/1.8/topics/auth/default/#the-login-required-decorator)

O seu template que responde pela index (`mysite/polls/index.html`) deve ser como o demonstrado abaixo.

```python
{% if user.is_authenticated %}
    <p>Bem vindo, {{ user.username }}

    <p>Área restrita...</p>

    {# Este é o link para logout #}
    <a href="{% url 'logout' %}">Logout</a>

{% endif %}
```

Agora devemos criar o template `mysite/polss/login.html` com o seguinte conteúdo:

```python
<form method="POST" action="{% url 'django.contrib.auth.views.login' %}">
    {% csrf_token %}

    {# Utilizamos o `form.as_p` para renderizar os inputs do formulário de login. #}
    {{ form.as_p }}

    <input type="submit" value="login" />
</form>
```

O [CSRF Token](https://docs.djangoproject.com/en/1.8/ref/csrf/) é obrigatório para o correto funcionamento da aplicação,
por ser um método POST é necessário colocar o `CSRF Token` no formulário.

O [forms.as_p](https://docs.djangoproject.com/en/1.8/ref/forms/api/#outputting-forms-as-html) também é obrigatório
para o correto funcionamento, pois de outra forma teríamos que saber qual o nome do campo que o Django está criando
automaticamente e, por tanto, não faz sentido não usar o __forms.as_p__.


