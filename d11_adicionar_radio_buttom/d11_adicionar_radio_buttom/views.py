from django.shortcuts import render
from d11_adicionar_radio_buttom.models import Radio

def index(request):
    listar_radios = Radio.objects.order_by('id')
    return render(request, 'd11_adicionar_radio_buttom/index.html', {'listar_radios':listar_radios})
    
def enviar(request):
    listar_radios = Radio.objects.order_by('id')
    
    if request.method == 'POST':
        radio_buttom = Radio.objects.create(
            label = request.POST['label'],
            name = request.POST['name'],
        )
        return render(request, 'd11_adicionar_radio_buttom/index.html', {'radio_buttom': radio_buttom, 'listar_radios':listar_radios})
    
    elif request.method == 'GET':
        return render(request, 'd11_adicionar_radio_buttom/index.html', {'listar_checkboxes':listar_checkboxes})