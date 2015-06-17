Criando um sistema de login customizado no Django
===


[https://docs.djangoproject.com/en/1.8/topics/auth/default/#how-to-log-a-user-in](https://docs.djangoproject.com/en/1.8/topics/auth/default/#how-to-log-a-user-in)

Podemos criar uma função de login na `view.py` utilizando os recursos que o Django
disponibiliza e adicionando outras funcionalidades tanto na view como no template.

Neste exemplo iremos adicionar uma frase na SESSION.

Veja mais sobre como utilizar a SESSION em [https://docs.djangoproject.com/en/1.8/topics/http/sessions/](https://docs.djangoproject.com/en/1.8/topics/http/sessions/)



View
---

Adicione as seguintes funções:

- O `index` para renderizar o formulário;

- O `acessar` para efetuar o login;

- O `usuario_logado` para quando o usuário estiver logado;

- O `sair` para quando o usuário sair do sistema.


E importe os módulos necessários...

    from django.shortcuts import render, redirect
    from django.contrib.auth import authenticate, login, logout
    from django.contrib.auth.decorators import login_required


### Na view acessar...

Adicione as linha abaixo:

    def acessar(request):
        # Inicialize as variáveis...
        usuario = senha = ''
        estado = "Digite seu Nome de usuário e senha."

        # Verifique se a requisição veio pelo método POST...
        if request.POST:

            usuario = request.POST.get('username')
            senha = request.POST.get('password')

            # Função do Django que autentica o usuário
            user = authenticate(username=usuario, password=senha)

            # Verifica se o usuário existe no banco de dados
            if user is not None:

                # Verifica se o status do usuário está ativado
                if user.is_active:

                    # Atribuímos na SESSION `frase` uma string ou qualquer outro valor
                    request.session['frase'] = "Uma string qualquer ou um resultado de uma pesquisa"

                    # Faz a requisição de login do usuário
                    login(request, user)

                    # Redireciona o usuário para a view `usuario_logado`
                    return redirect('login.views.usuario_logado')

                # Caso o usuário não estiver com status ativado, envia a mensagem de erro
                else:
                    status = "Usuário não está ativo"

            # Caso o usuário não exista na base de dados
            else:
                status = "Usuário ou senha incorreto"

        return render(request, 'login/index.html', {'status': status, 'username': usuario})



### Na view usuario_logado...

Adicione o decorator `login_required` na função

    @login_required(login_url='/')
    def usuario_logado(request):
        # Inicializa a variável `frase` como dicionário
        frase = {}

        # Verifica se a requisição possui a 'frase' na sessão
        if 'frase' in request.session:
            lista['frase']    = request.session['frase']
            lista['opcional'] = 'Uma sting qualquer'
            lista['numeros']  = 1234567890

        else:
            lista['frase']    = ''
            lista['opcional'] = ''
            lista['numeros']  = ''

        return render(request, 'login/home.html', {'lista': lista})

        

### Na view sair...

Adicione a função `logout` do Django

    def sair(request):
        logout(request)
        return redirect('login_session.views.index')



Url
---

Adicione as urls das páginas...

    url(r'^$', views.index, name='index'),
    url(r'^acessar/$', views.acessar, name='acessar'),
    url(r'^sair/$', views.sair, name='sair'),
    url(r'^usuario_logado/$', views.usuario_logado, name='usuario_logado'),



Templates
---

No template `index` adicionamos o formulário de login. Ao invés de utilizarmos o `form.as_p`, 
criamos o formulário em HTML.

    <form method="POST" action="{% url 'acessar' %}">
        {% csrf_token %}
        {% if next %}
            <input type="hidden" name="next" value="{{ next }}" />
        {% endif %}
        <label for='usuario'>Usuário: </label>
        <input type="text" name="username" id="usuario" value="{{ username }}" /><br />
        <label for="senha">Senha: </label>
        <input type="password" name="password" id="senha" value="" /><br />

        <input type="submit" value="Log In" />
    </form>


Para visualizar as mensagens de erro do login na página adicione...

    {% if status %}
        {{status}}
    {% endif %}



No template `home` adicione a área do usuário quando estiver logado.

    {% if user.is_authenticated %}
        <p>Bem vindo, {{ user.username }}  <a href="{% url 'logout' %}">[logout]</a></p>
        <p>Área protegida pelo sistema de login do Django.</p>
        
        # Renderiza contexto enviado pela view 
        {% if lista %}
            Session: {{lista.frase}}
            Session: {{lista.frase2}}
            Session: {{lista.frase3}}
        {% endif %}

    {% else %}
        <p>Bem vindo, Visitante <a href="/">[login]</a></p>

    {% endif %}