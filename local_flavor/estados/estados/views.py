from django.shortcuts import render
from local_flavor_estados.forms import ComboboxForm
from local_flavor_estados.models import Combobox

def index(request):    
    listar = Combobox.objects.order_by('-id')
    
    form = ComboboxForm()
    return render(request, 'local_flavor_estados/index.html', {'form': form, 'listar': listar})
    
def enviar(request):
    if request.method == 'POST':
        form = Combobox.objects.create(
            estado = request.POST['estado'],
        )
        
        return render(request, 'local_flavor_estados/enviado.html', {'form': form})
    return render(request, 'local_flavor_estados/enviado.html', {})
