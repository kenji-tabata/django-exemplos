Requisições GET e POST
===

Como receber um requisição GET:

def foo(request):
    context = {}
    
    if request.method == 'GET':
        if request.GET.__contains__('nome'):
            context['nome'] = request.GET['nome']
            
    return render(request, 'app/index.html', context)

Como receber um requisição POST:

def foo(request):
    context = {}
    
    if request.method == 'POST':
        if request.POST.__contains__('nome'):
            context['nome'] = request.POST['nome']
            
    return render(request, 'app/result.html', context)

Lembrando que o formulário que enviar os dados pelo método post deverá conter o [csrf_token](csrf_token.md)

    ...
    ...
    ...
    {% csrf_token %}
    ...
    ...
    ...
