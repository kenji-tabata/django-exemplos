from django.shortcuts import render

def index(request):
    return render(request, 'javascript02/index.html', {})

