from django.shortcuts import render
from d09_adicionar_checkbox.models import Post

def index(request):
    listar_checkboxes = Post.objects.order_by('id')
    return render(request, 'd09_adicionar_checkbox/index.html', {'listar_checkboxes':listar_checkboxes})
    
def enviar(request):
    listar_checkboxes = Post.objects.order_by('id')
    
    if request.method == 'POST':
        checkbox = Post.objects.create(
            label = request.POST['label'],
        )
        return render(request, 'd09_adicionar_checkbox/index.html', {'checkbox': checkbox, 'listar_checkboxes':listar_checkboxes})
    
    elif request.method == 'GET':
        return render(request, 'd09_adicionar_checkbox/index.html', {'listar_checkboxes':listar_checkboxes})