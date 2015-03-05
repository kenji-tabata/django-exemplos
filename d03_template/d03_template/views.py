from django.shortcuts import render

def index(request):
    return render(request, 'd03_template/index.html', {})

def pagina(request):
    return render(request, 'd03_template/pagina.html', {})

def base(request):
    return render(request, 'd03_template/base.html', {})