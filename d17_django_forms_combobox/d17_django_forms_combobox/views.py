from django.shortcuts import render
from d17_django_forms_combobox.forms import ComboboxForm
from d17_django_forms_combobox.models import Combobox

def index(request):
    listar_combo = Combobox.objects.order_by('-id')
    
    form = ComboboxForm()
    return render(request, 'd17_django_forms_combobox/index.html', {'form': form, 'listar_combo': listar_combo})
    
def enviar(request):
    if request.method == 'POST':
        combobox = Combobox.objects.create(
            tipo = request.POST['tipo']
        )
        return render(request, 'd17_django_forms_combobox/enviado.html', {'combobox': combobox})
    return render(request, 'd17_django_forms_combobox/enviado.html', {})