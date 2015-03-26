from django.shortcuts import render
from f01_models.models import Post

def index(request):
    listar_posts = Post.objects.order_by('-data')
    return render(request, 'f01_models/index.html', {'listar_posts':listar_posts})
