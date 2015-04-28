from django.shortcuts import render

def index(request):
    context = {}
    
    if request.method == 'GET':
        if request.GET.__contains__('nome'):
            context['nome'] = request.GET['nome']
            
    return render(request, 'metodo_get/index.html', context)
