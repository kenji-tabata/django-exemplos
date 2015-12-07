from django.shortcuts import render, redirect
from textbox.models import Postagens

def index(request):
    return render(request, 'textbox/index.html', {})

def listar(request):
    listar_posts = Postagens.objects.order_by('-data')
    
    return render(request, 'textbox/listar.html', {'listar_posts':listar_posts})

def enviar(request):
    if request.method == 'POST':
        postagem = Postagens.objects.create(
            titulo = request.POST['titulo'],
            email = request.POST['email'],
            url = request.POST['url'],
            rating = request.POST['rating'],
            like = request.POST['like'],
            conteudo = request.POST['conteudo'],
        )
        
        return redirect('textbox:textbox.views.listar')
    
    return render(request, 'app/index.html', {})