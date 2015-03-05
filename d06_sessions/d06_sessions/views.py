from django.shortcuts import render


def index(request):
    if request.method == 'GET':
        if request.GET.__contains__('nome'):
            request.session['nome'] = request.GET['nome']
            
    elif request.method == 'POST':
        if request.POST.__contains__('sobrenome'):
            request.session['sobrenome'] = request.POST['sobrenome']
            
    return render(request, 'd06_sessions/index.html', {})

def getNome(request):
    context = {}
    
    if request.session.__contains__('nome') and request.session.__contains__('sobrenome'):
        if len(request.session['nome']) > 0:
            context['nome'] = request.session['nome']
        else:
            context['nome'] = ""
            
        if len(request.session['sobrenome']) > 0:
            context['sobrenome'] = request.session['sobrenome']
        else:
            context['sobrenome'] = ""
    else:
        context['nome'] = "Não foi encontrado nenhum nome na Session." 

    return render(request, 'd06_sessions/index.html', context)