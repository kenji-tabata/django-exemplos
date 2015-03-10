from django.shortcuts import render
from d16_django_forms_radiobutton.forms import RadioForm
from d16_django_forms_radiobutton.models import Radio

def index(request):
    listar_radio = Radio.objects.order_by('-id')
    
    form = RadioForm()
    return render(request, 'd16_django_forms_radiobutton/index.html', {'form': form, 'listar_radio': listar_radio})
    
def enviar(request):
    
    if request.method == 'POST':
        radio = Radio.objects.create(
            sexo = request.POST['sexo'],            
        )
        return render(request, 'd16_django_forms_radiobutton/enviado.html', {'radio': radio})
    return render(request, 'd16_django_forms_radiobutton/enviado.html', {})