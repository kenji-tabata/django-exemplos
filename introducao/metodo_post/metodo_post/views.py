from django.shortcuts import render

def index(request):
    return render(request, 'metodo_post/index.html', {})

def result(request):
    context = {}
    
    if request.method == 'POST':
        if request.POST.__contains__('nome'):
            context['nome'] = request.POST['nome']
            
    return render(request, 'metodo_post/result.html', context)

