from django.shortcuts import render
from f06_checkbox_multi.models import Check

def ret_checks():
    checkboxes = {}
    checkboxes[1] = "primeira frase"
    checkboxes[2] = "segunda frase"
    checkboxes[3] = "terceira frase"
    checkboxes[4] = "quarta frase"
    checkboxes[5] = "quinta frase"
    checkboxes[6] = "sexta frase"
    checkboxes[7] = "setima frase"
    checkboxes[8] = "oitava frase"
    checkboxes[9] = "nona frase"
    checkboxes[10] = "decima frase"
    
    return checkboxes

def index(request):
    lista = Check.objects.order_by('-id')
    checkboxes = ret_checks()
    return render(request, 'f06_checkbox_multi/index.html', {'checkboxes': checkboxes, 'lista': lista})

def enviar(request):
    lista = Check.objects.order_by('-id')
    checkboxes = ret_checks()
    
    if request.method == 'POST':
        resp = Check.objects.create(
            nome = request.POST['nome'],
            alternativa = request.POST.getlist('check'), # função getlist() recupera os dados selecionados dos checkboxes.
        )
        return render(request, 'f06_checkbox_multi/index.html', {'resp': resp, 'checkboxes': checkboxes, 'lista': lista})
    
    elif request.method == 'GET':
        return render(request, 'f06_checkbox_multi/index.html', {'checkboxes': checkboxes})
