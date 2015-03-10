from django.shortcuts import render
from d15_django_forms_checkbox.forms import CheckboxForm
from d15_django_forms_checkbox.models import CheckBox

def index(request):
    listar_check = CheckBox.objects.order_by('-id')
    
    form = CheckboxForm()
    return render(request, 'd15_django_forms_checkbox/index.html', {'form': form, 'listar_check': listar_check})
    
def enviar(request):
    if request.method == 'POST':
        checkbox = CheckBox.objects.create(
            email = request.POST['email'],
            assinar = request.POST.get('assinar', False), # Paramêtro False caso o checkbox não for selecionado
        )
        return render(request, 'd15_django_forms_checkbox/enviado.html', {'checkbox': checkbox})
    return render(request, 'd15_django_forms_checkbox/enviado.html', {})