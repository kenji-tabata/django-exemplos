from django.shortcuts import render
from datetime import datetime
from textbox.models import Post

def index(request):
    listar_posts = Post.objects.order_by('-data')
    return render(request, 'textbox/index.html', {'listar_posts':listar_posts})
    
def enviar(request):
    if request.method == 'POST':
        listar_posts = Post.objects.order_by('-data')
        
        post = Post.objects.create(
            titulo = request.POST['titulo'],
            data = datetime.now(),
            conteudo = request.POST['conteudo'],
        )
        return render(request, 'textbox/index.html', {'post': post, 'listar_posts':listar_posts})
    
    elif request.method == 'GET':
        return render(request, 'textbox/index.html', {'posts':posts})