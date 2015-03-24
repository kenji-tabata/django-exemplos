from django.shortcuts import render
from d20_django_forms_input_hidden.forms import HiddenForm
from d20_django_forms_input_hidden.models import Hidden

def index(request):
    listar_text = Hidden.objects.order_by('-id')
    
    form = HiddenForm()
    return render(request, 'd20_django_forms_input_hidden/index.html', {'form': form,'listar_text': listar_text})
    
def enviar(request):
    if request.method == 'POST':
        textbox = Hidden.objects.create(
            nome = request.POST['nome'],
            dado = request.POST['dado'],
        )
        return render(request, 'd20_django_forms_input_hidden/enviado.html', {'textbox': textbox})
    return render(request, 'd20_django_forms_input_hidden/enviado.html', {})