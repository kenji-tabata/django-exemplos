from django.shortcuts import render

def index(request):
    return render(request, 'dj_01_hello_world/index.html', {})
