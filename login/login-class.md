Criando um sistema de login com classe auxiliar no Django
===


Possui as mesmas funções do [Criando um sistema de login customizado no Django](login-custom.md) sendo 
a sua principal diferença está na criação de uma classe para separar da view as funções do login.


Crie uma classe `LoginUsuario` e importe os módulos necessários...

    from django.contrib.auth import authenticate, login

    class LoginUsuario(object):


Adicione a função de autenticação do usuário...

    def autenticar_usuario (self, request, usuario, senha):
        
        # Função do Django que autentica o usuário
        user = authenticate(username=usuario, password=senha)
        
            # Verifica se o usuário existe no banco de dados
            if user is not None:

                # Verifica se o status do usuário está ativado
                if user.is_active:

                # Envia o objeto `user` para adicionar seus dados na sessão
                self.set_session(request, user)
                
                login(request, user)
                return True
            else:
                return 'desativado'
        else:
            return False


Para utilizar a SESSION criamos as funções get_session e set_session para salvar 
e recuperar o valor da sessão.

    def set_session(self, request, usuario):
        # O argumento `usuario` é um objeto da classe `user` do Django
        request.session['primeiro-nome'] = usuario.first_name
        request.session['nome-usuario'] = usuario.username


    def get_session(self, request, keys)
        lista = {}

        # O argumento `keys` recebe um array
        for key in keys:
            if key in request.session:
                lista[key] = request.session[key]

            else:
                lista['primeiro-nome'] = ''

        # Retorna uma lista na forma de dicionário
        return lista



View
---

A função `acessar` da view fica encarregado apenas de fazer o redirecionamento.

Para as funções do login funcionar é preciso importar a classe `LoginUsuario`...

    # O `usuario` é o nome do arquivo (módulo)
    from login.usuario import LoginUsuario


Crie o objeto LoginUsuario para acessar suas funções

    login_usuario = LoginUsuario()


E adicione as linhas abaixo

    if request.POST:
        usuario = request.POST.get('username')
        senha = request.POST.get('password')

        # O `autorizacao` recebe o resultado da função do login
        autorizado = login_usuario.autenticar_usuario(request, usuario, senha)


        if autorizado == True:
            # Redireciona para a página de usuário logado
            return redirect('home')

        # Modifica o status pelas mensagens de erro.
        elif (autorizado == 'desativado'):
            status = 'O usuário não está com o status ativado.'
        else:
            status = 'O usuário ou senha está incorreto.'
    
    return render(request, 'login_class/index.html', {'status': status, 'username': username})


A função `usuario_logado` apenas recupera a informação que está armazenada na 
SESSION e renderiza a página.

    @login_required(login_url='/')
    def usuario_logado(request):
        # Cria um array com os nomes das keys de cada parâmetro da sessão
        keys = ['primeiro_nome', 'nome_usuario']

        # Recupera da sessão o valor de cada chave do array `keys`
        session_usuario = LoginUsuario().get_session(request, keys)

        return render(request, 'login/home.html', {'session_usuario': session_usuario})



