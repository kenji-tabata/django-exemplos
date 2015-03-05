from django.shortcuts import render

def index(request):
    context = {}
    
    if request.method == 'GET':
        if request.GET.__contains__('nome'):
            context['nome'] = request.GET['nome']
            
    return render(request, 'd04_metodo_get/index.html', context)
