from django.shortcuts import render
from textbox_forms.forms import TextboxForm
from textbox_forms.models import TextBox

def index(request):
    listar_text = TextBox.objects.order_by('-data')
    
    form = TextboxForm()
    return render(request, 'textbox_forms/index.html', {'form': form,'listar_text': listar_text})
    
def enviar(request):
    if request.method == 'POST':
        textbox = TextBox.objects.create(
            nome = request.POST['nome'],
            email = request.POST['email'],
            url = request.POST['url'],
            data = request.POST['data'],
            valor = request.POST['valor'],
            numero = request.POST['numero'],
            mensagem = request.POST['mensagem'],
            senha = request.POST['senha'],
        )
        return render(request, 'textbox_forms/enviado.html', {'textbox': textbox})
    return render(request, 'textbox_forms/enviado.html', {})