from django.shortcuts import render
from d22_django_forms_listar_estados.forms import ComboboxForm
from d22_django_forms_listar_estados.models import Combobox

def index(request):    
    listar = Combobox.objects.order_by('-id')
    
    form = ComboboxForm()
    return render(request, 'd22_django_forms_listar_estados/index.html', {'form': form, 'listar': listar})
    
def enviar(request):
    if request.method == 'POST':
        form = Combobox.objects.create(
            estado = request.POST['estado'],
        )
        
        return render(request, 'd22_django_forms_listar_estados/enviado.html', {'form': form})
    return render(request, 'd22_django_forms_listar_estados/enviado.html', {})
