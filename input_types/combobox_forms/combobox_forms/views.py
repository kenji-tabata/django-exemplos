from django.shortcuts import render
from combobox_forms.forms import ComboboxForm
from combobox_forms.models import Combobox

def index(request):
    listar_combo = Combobox.objects.order_by('-id')
    
    form = ComboboxForm()
    return render(request, 'combobox_forms/index.html', {'form': form, 'listar_combo': listar_combo})
    
def enviar(request):
    if request.method == 'POST':
        combobox = Combobox.objects.create(
            tipo = request.POST['tipo']
        )
        return render(request, 'combobox_forms/enviado.html', {'combobox': combobox})
    return render(request, 'combobox_forms/enviado.html', {})