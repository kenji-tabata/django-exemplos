from django.shortcuts import render, redirect
from textbox_forms.models import Postagem
from textbox_forms.forms import PostagensForm

def index(request):
    return render(request, 'textbox_forms/index.html', {})

def listar(request):
    listar_posts = Postagem.objects.order_by('-data')
    
    return render(request, 'textbox_forms/listar.html', {'listar_posts':listar_posts})

def enviar(request):
    if request.method == 'POST':
        form = PostagensForm(request.POST)
        if form.is_valid():
            form_valid = form.save(commit=False)
            form_valid.save()
        
            return redirect('textbox_forms:textbox_forms.views.listar')
    
    return render(request, 'textbox_forms/index.html', {})