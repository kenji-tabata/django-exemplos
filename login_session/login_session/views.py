from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

def index(request):
    status = "Digite seu Nome de usuário e senha."
    return render(request, 'login_session/index.html', {'status': status})

def login_user(request):
    username = password = ''
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session['frase'] = "1234"
                print("Definindo a frase da Session: "+request.session['frase'])
                
                login(request, user)
                return redirect('login_session.views.logado')
            else:
                status = "Usuário não está ativo"
                
        else:
            status = "Usuário ou senha incorreto"
            
    return render(request, 'login_session/index.html', {'status': status, 'username': username})

# Decorator que redireciona o usuário para a tela de login caso não esteja logado no sistema
# fata aqui o decorator
def logado(request):
    context = {}
    
    try:
        print("logado "+request.session['frase'])
        
        if request.session.__contains__('frase'):
            context['frase'] = request.session['frase']
            print("Carregando a frase gravada na seção: %s" % (context['frase']))
        else:
            context['frase'] = ""
            
        return render(request, 'login_session/logado.html', context)
    
    except KeyError as e:
        print ('O parâmetro %s da SESSION não foi encontrada.' % (e))
        return redirect('login_session.views.index')

    