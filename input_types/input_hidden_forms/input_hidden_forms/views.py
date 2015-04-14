from django.shortcuts import render
from input_hidden_forms.forms import HiddenForm
from input_hidden_forms.models import Hidden

def index(request):
    listar_text = Hidden.objects.order_by('-id')
    
    form = HiddenForm()
    return render(request, 'input_hidden_forms/index.html', {'form': form,'listar_text': listar_text})
    
def enviar(request):
    if request.method == 'POST':
        textbox = Hidden.objects.create(
            nome = request.POST['nome'],
            dado = request.POST['dado'],
        )
        return render(request, 'input_hidden_forms/enviado.html', {'textbox': textbox})
    return render(request, 'input_hidden_forms/enviado.html', {})