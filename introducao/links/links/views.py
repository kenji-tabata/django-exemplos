from django.shortcuts import render

def index(request):
    return render(request, 'links/index.html', {})

def pagina01(request):
    return render(request, 'links/pagina01.html', {})

def pagina02(request):
    return render(request, 'links/pagina02.html', {})