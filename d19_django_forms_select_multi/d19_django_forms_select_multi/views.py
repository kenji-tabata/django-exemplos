from django.shortcuts import render
from d19_django_forms_select_multi.forms import SelectForm
from d19_django_forms_select_multi.models import Select

def index(request):
    listar_select = Select.objects.order_by('-id')
    
    form = SelectForm()
    return render(request, 'd19_django_forms_select_multi/index.html', {'form': form,'listar_select': listar_select})
    
def enviar(request):
    if request.method == 'POST':
        select = Select.objects.create(
            tipo = request.POST.getlist('tipo'),
        )
        return render(request, 'd19_django_forms_select_multi/enviado.html', {'select': select})
    return render(request, 'd19_django_forms_select_multi/enviado.html', {})