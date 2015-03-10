from django.shortcuts import render
from d14_django_forms_textbox.forms import TextboxForm
from d14_django_forms_textbox.models import TextBox

def index(request):
    listar_text = TextBox.objects.order_by('-data')
    
    form = TextboxForm()
    return render(request, 'd14_django_forms_textbox/index.html', {'form': form,'listar_text': listar_text})
    
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
        return render(request, 'd14_django_forms_textbox/enviado.html', {'textbox': textbox})
    return render(request, 'd14_django_forms_textbox/enviado.html', {})