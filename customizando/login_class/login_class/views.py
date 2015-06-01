from django.shortcuts import render, redirect
from login_class.usuario import Usuario
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'login_class/index.html', {})

def login_user(request):
    status = "Digite seu nome de usuário e senha."
    username = ""
    
    usuario = Usuario()
    
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        if usuario.auth_user(request, username, password) == True:
            return redirect('home')
        else:
            status = usuario.auth_user(request, username, password)
    
    return render(request, 'login_class/index.html', {'status': status, 'username': username})

@login_required(login_url='/')
def home(request):
    # Array das SESSIONS que serão utilizadas na página
    dados = ['nome_usuario', 'usuario']
    
    # Utiliza o Array dados para carregar as variáveis da SESSION
    session_usuario = Usuario().get_user_session(request, dados)
    
    return render(request, 'login_class/home.html', {'session_usuario': session_usuario})

