from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'd09_login/index.html', {})

@login_required(login_url='/')
def logado(request):
    return render(request, 'd09_login/logado.html', {})