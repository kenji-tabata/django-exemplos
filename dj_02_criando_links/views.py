from django.shortcuts import render

def index(request):
    return render(request, 'dj_02_criando_links/index.html', {})

def pagina01(request):
    return render(request, 'dj_02_criando_links/pagina01.html', {})

def pagina02(request):
    return render(request, 'dj_02_criando_links/pagina02.html', {})