Utilizando o sistema de Login padrão do Django
===


[https://docs.djangoproject.com/en/1.8/topics/auth/default/#using-the-django-authentication-system](https://docs.djangoproject.com/en/1.8/topics/auth/default/#using-the-django-authentication-system)

Login
---


A forma mais simples de se utilizar o login do Django é utilizando a classe 
`django.contrib.auth.views.login` no template.


Primeiro criamos o formulário de login no template...

    <form method="POST" action="{% url 'django.contrib.auth.views.login' %}">
        # Por ser um método POST é necessário colocar o `CSRF Token` no formulário...
        {% csrf_token %}

        # Utilizamos o `form.as_p` para renderizar os inputs do formulário de login.
        {{ form.as_p }}

        <input type="submit" value="login" />
    </form>


No `urls.py` definimos a url que irá renderizar o formulário de login...

    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login/login.html','redirect_field_name': ''}, name='login'),


E a url que o usuário será redirecionado quando efetuar o login

    url(r'^$', views.index, name='index'),


Configure no `settings.py` a página que o usuário será redirecionado após efetuar o login. 
No exemplo definimos o redirecionamento para o `index`.

    LOGIN_REDIRECT_URL = '/'


Na `view.py` importe o decorator `login_required` 

    from django.contrib.auth.decorators import login_required


Adicione as funções `index` e `login` 

    def index(request):
        return render(request, 'login/index.html', {})

    def login(request):
        return render(request, 'login/login.html', {})


E bloqueia o acesso a página `index.html` quando o usuário não estiver logado, 
ao adicionar o decorator `login_required` acima da função `index`.

    @login_required(login_url='/login')
    def index(request):


No template adicione um bloco if que verifica se o usuário está logado 

    {% if user.is_authenticated %}
        <p>Bem vindo, {{ user.username }}  <a href="/logout">[logout]</a></p>

        <p>Área restrita...</p>

    {% endif %}


Para testar crie um usuário pelo terminal

    python manage.py createsuperuser

Veja mais como `criar um usuário` em [https://docs.djangoproject.com/en/1.8/topics/auth/default/#creating-users](https://docs.djangoproject.com/en/1.8/topics/auth/default/#creating-users)


E acesse [127.0.0.1:8000](127.0.0.1:8000)



Logout
---

Adicione no `urls.py` a url para sair do sistema

    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/login'}),


E no template adicione o link para sair

     <a href="{% url 'logout' %}">Logout</a>






Veja mais sobre o `CSRF Token` em [https://docs.djangoproject.com/en/1.8/ref/csrf/](https://docs.djangoproject.com/en/1.8/ref/csrf/).

Veja mais sobre o `forms.as_p` em [https://docs.djangoproject.com/en/1.8/ref/forms/api/#outputting-forms-as-html](https://docs.djangoproject.com/en/1.8/ref/forms/api/#outputting-forms-as-html).

