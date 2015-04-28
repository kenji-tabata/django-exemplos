from django.shortcuts import render
from models.models import Post

def index(request):
    listar_posts = Post.objects.order_by('-data')
    return render(request, 'models/index.html', {'listar_posts':listar_posts})
