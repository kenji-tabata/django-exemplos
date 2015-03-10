from django.shortcuts import render
from d18_django_forms_checkbox_multi.forms import CheckboxForm
from d18_django_forms_checkbox_multi.models import CheckBox

def index(request):
    listar_check = CheckBox.objects.order_by('-id')
    
    form = CheckboxForm()
    return render(request, 'd18_django_forms_checkbox_multi/index.html', {'form': form,'listar_check': listar_check})
    
def enviar(request):
    if request.method == 'POST':
        checkbox = CheckBox.objects.create(
            tipo = request.POST.getlist('tipo'),
        )
        return render(request, 'd18_django_forms_checkbox_multi/enviado.html', {'checkbox': checkbox})
    return render(request, 'd18_django_forms_checkbox_multi/enviado.html', {})