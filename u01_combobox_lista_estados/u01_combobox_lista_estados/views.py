from django.shortcuts import render
from u01_combobox_lista_estados.forms import ComboboxForm
from u01_combobox_lista_estados.models import Combobox

def index(request):    
    listar = Combobox.objects.order_by('-id')
    
    form = ComboboxForm()
    return render(request, 'u01_combobox_lista_estados/index.html', {'form': form, 'listar': listar})
    
def enviar(request):
    if request.method == 'POST':
        form = Combobox.objects.create(
            estado = request.POST['estado'],
        )
        
        return render(request, 'u01_combobox_lista_estados/enviado.html', {'form': form})
    return render(request, 'u01_combobox_lista_estados/enviado.html', {})
