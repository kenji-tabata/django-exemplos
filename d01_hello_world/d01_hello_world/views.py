from django.shortcuts import render

def index(request):
    return render(request, 'd01_hello_world/index.html', {})
