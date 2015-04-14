from django.shortcuts import render
from django.shortcuts import redirect

from local_flavor_form_validacao.forms import ClienteForm
from local_flavor_form_validacao.models import Cliente

def index(request):    
    listar = Cliente.objects.order_by('-id')
    
    form = ClienteForm()
    return render(request, 'local_flavor_form_validacao/index.html', {'form': form, 'listar': listar})
    
def enviar(request):
    listar = Cliente.objects.order_by('-id')
    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('local_flavor_form_validacao.views.enviar')
    else:
        form = ClienteForm()
    return render(request, 'local_flavor_form_validacao/index.html', {'form': form, 'listar': listar})
        
