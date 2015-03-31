from django.shortcuts import render
from f08_radio_button.models import Radio

def index(request):
    listar_radios = Radio.objects.order_by('id')
    return render(request, 'f08_radio_button/index.html', {'listar_radios':listar_radios})
    
def enviar(request):
    listar_radios = Radio.objects.order_by('id')
    
    if request.method == 'POST':
        radio_buttom = Radio.objects.create(
            sexo = request.POST['sexo'],
        )
        return render(request, 'f08_radio_button/index.html', {'radio_buttom': radio_buttom, 'listar_radios':listar_radios})
    
    elif request.method == 'GET':
        return render(request, 'f08_radio_button/index.html', {'listar_radios':listar_radios})