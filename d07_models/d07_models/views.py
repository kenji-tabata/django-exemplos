from django.shortcuts import render
from datetime import datetime
from d07_models.models import Post

def index(request):
    listar_posts = Post.objects.order_by('-data')
    return render(request, 'd07_models/index.html', {'listar_posts':listar_posts})
    
def enviar(request):
    if request.method == 'POST':
        listar_posts = Post.objects.order_by('-data')
        
        post = Post.objects.create(
            titulo = request.POST['titulo'],
            data = datetime.now(),
            conteudo = request.POST['conteudo'],
        )
        return render(request, 'd07_models/index.html', {'post': post, 'listar_posts':listar_posts, 'sucess': "Post adicionado com sucesso."})
    
    elif request.method == 'GET':
        return render(request, 'd07_models/index.html', {'posts':posts})