from django.shortcuts import render, redirect
from ajax_csrf.forms import UsuarioForm
from ajax_csrf.forms import ComentarioForm
from ajax_csrf.models import Usuario
from ajax_csrf. models import Comentario
import json

def index(request):
    form = UsuarioForm()
    listar_usuarios = Usuario.objects.order_by('-id')
        
    form_comment = ComentarioForm()
    listar_comentarios = Comentario.objects.order_by('-id')
    
    return render(request, 'ajax_csrf/index.html', {
        'form': form, 
        'listar_usuarios': listar_usuarios, 
        'form_comment': form_comment, 
        'listar_comentarios': listar_comentarios
    })
'''
    Recebe os dados do formulário padrão por AJAX e faz a validação automática do Django
'''
def enviar(request):
    form = UsuarioForm()
    listar_usuarios = Usuario.objects.order_by('-id')
    
    form_comment = ComentarioForm()
    listar_comentarios = Comentario.objects.order_by('-id')
    
  
    if request.method == 'POST':
        if request.is_ajax():
            print(request.POST)

        form = UsuarioForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            return redirect('ajax_csrf.views.index') 
        else:
            print('Erro: Não preencheu todos os dados')

    else:
        form = UsuarioForm
        
    return render(request, 'ajax_csrf/index.html', {
        'form': form, 
        'listar_usuarios': listar_usuarios, 
        'form_comment': form_comment, 
        'listar_comentarios': listar_comentarios
    })


'''
    Recebe um objeto JSON do formulário por AJAX e faz a validação automática do Django
'''
def enviar_comentario(request):
    form = UsuarioForm()
    listar_usuarios = Usuario.objects.order_by('-id')
    
    form_comment = ComentarioForm()
    listar_comentarios = Comentario.objects.order_by('-id')
    
    if request.method == 'POST':
        if request.is_ajax():
            json_decode = json.loads(request.POST.get('comentario'))
            form_comment = ComentarioForm(json_decode)
            print(json_decode)
        
        else:
            form_comment = ComentarioForm(request.POST)
            print(request.POST)
        
        if form_comment.is_valid():
            comentario = form_comment.save()
            return redirect('ajax_csrf.views.index') 
        else:
            print('Erro: Não preencheu todos os dados')

    else:
        form = ComentarioForm

    return render(request, 'ajax_csrf/index.html', {
        'form': form, 
        'listar_usuarios': listar_usuarios, 
        'form_comment': form_comment, 
        'listar_comentarios': listar_comentarios
    })
