from django.shortcuts import render
from testando_model.models import Contato

def index(request):
    contatos = Contato.objects.order_by('-id')
    return render(request, 'testando_model/index.html', {'contatos': contatos})
