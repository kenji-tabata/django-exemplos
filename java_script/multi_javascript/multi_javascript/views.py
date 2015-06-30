from django.shortcuts import render

def index(request):
    return render(request, 'multi_javascript/index.html', {})

def pagina(request):
    return render(request, 'multi_javascript/pagina.html', {})