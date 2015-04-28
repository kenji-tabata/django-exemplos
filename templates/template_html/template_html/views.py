from django.shortcuts import render

def index(request):
    return render(request, 'template_html/index.html', {})

def pagina(request):
    return render(request, 'template_html/pagina.html', {})

def base(request):
    return render(request, 'template_html/base.html', {})