from django.shortcuts import render
from multi_database_intro.models import Post

def index(request):
    posts = Post.objects.using('default').order_by('titulo')
    return render(request, 'multi_database_intro/index.html', {'posts': posts})

def trocar(request, tipo):
    posts = Post.objects.using(tipo).order_by('titulo')
    return render(request, 'multi_database_intro/index.html', {'posts': posts, 'tipo': tipo})