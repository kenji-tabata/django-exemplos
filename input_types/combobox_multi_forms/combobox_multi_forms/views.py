from django.shortcuts import render
from combobox_multi_forms.forms import SelectForm
from combobox_multi_forms.models import Select

def index(request):
    listar_select = Select.objects.order_by('-id')
    
    form = SelectForm()
    return render(request, 'combobox_multi_forms/index.html', {'form': form,'listar_select': listar_select})
    
def enviar(request):
    if request.method == 'POST':
        select = Select.objects.create(
            tipo = request.POST.getlist('tipo'),
        )
        return render(request, 'combobox_multi_forms/enviado.html', {'select': select})
    return render(request, 'combobox_multi_forms/enviado.html', {})