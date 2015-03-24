from django.shortcuts import render

def index(request):
    return render(request, 'd00_base_projeto/index.html', {})