from django.shortcuts import render
from f09_radio_button_forms.forms import RadioForm
from f09_radio_button_forms.models import Radio

def index(request):
    listar_radio = Radio.objects.order_by('-id')
    
    form = RadioForm()
    return render(request, 'f09_radio_button_forms/index.html', {'form': form, 'listar_radio': listar_radio})
    
def enviar(request):
    
    if request.method == 'POST':
        radio = Radio.objects.create(
            sexo = request.POST['sexo'],            
        )
        return render(request, 'f09_radio_button_forms/enviado.html', {'radio': radio})
    return render(request, 'f09_radio_button_forms/enviado.html', {})