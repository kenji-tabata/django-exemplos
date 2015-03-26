from django.shortcuts import render
from f04_checkbox.models import Assinatura

def index(request):
    listar_checkboxes = Assinatura.objects.order_by('id')
    return render(request, 'f04_checkbox/index.html', {'listar_checkboxes':listar_checkboxes})
    
def enviar(request):
    listar_checkboxes = Assinatura.objects.order_by('id')
    
    if request.method == 'POST':
        checkbox = Assinatura.objects.create(
            email = request.POST['email'],
            assina = request.POST.get('assina', "Não desejo receber e-mail"),
        )
        return render(request, 'f04_checkbox/index.html', {'checkbox': checkbox, 'listar_checkboxes':listar_checkboxes})
    
    elif request.method == 'GET':
        return render(request, 'f04_checkbox/index.html', {'listar_checkboxes':listar_checkboxes})