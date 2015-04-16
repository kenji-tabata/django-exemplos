from django.shortcuts import render

def index(request):
    return render(request, 'javascript01/index.html', {})
