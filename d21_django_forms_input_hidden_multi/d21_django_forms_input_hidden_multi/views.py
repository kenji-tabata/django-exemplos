from django.shortcuts import render
from d21_django_forms_input_hidden_multi.forms import HiddenForm
from d21_django_forms_input_hidden_multi.models import Hidden

def index(request):
    listar_text = Hidden.objects.order_by('-id')
    
    form = HiddenForm()
    return render(request, 'd21_django_forms_input_hidden_multi/index.html', {'form': form,'listar_text': listar_text})
    
def enviar(request):
    if request.method == 'POST':
        textbox = Hidden.objects.create(
            nome = request.POST['nome'],
            dado = request.POST.getlist('dado'),
        )
        return render(request, 'd21_django_forms_input_hidden_multi/enviado.html', {'textbox': textbox})
    return render(request, 'd21_django_forms_input_hidden_multi/enviado.html', {})