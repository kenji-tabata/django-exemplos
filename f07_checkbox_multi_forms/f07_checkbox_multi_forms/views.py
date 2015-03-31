from django.shortcuts import render
from f07_checkbox_multi_forms.forms import CheckboxForm
from f07_checkbox_multi_forms.models import CheckBox

def index(request):
    listar_check = CheckBox.objects.order_by('-id')
    
    form = CheckboxForm()
    return render(request, 'f07_checkbox_multi_forms/index.html', {'form': form,'listar_check': listar_check})
    
def enviar(request):
    if request.method == 'POST':
        checkbox = CheckBox.objects.create(
            tipo = request.POST.getlist('tipo'),
        )
        return render(request, 'f07_checkbox_multi_forms/enviado.html', {'checkbox': checkbox})
    return render(request, 'f07_checkbox_multi_forms/enviado.html', {})