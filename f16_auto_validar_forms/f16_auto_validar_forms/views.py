from django.shortcuts import render
from django.shortcuts import redirect
from f16_auto_validar_forms.forms import FormularioForm
from f16_auto_validar_forms.models import Formulario

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('f16_auto_validar_forms.views.listar')
    else:
        form = FormularioForm()
        
    return render(request, 'f16_auto_validar_forms/index.html', {'form': form})


def listar(request):
    listar = Formulario.objects.order_by('-id')
    return render(request, 'f16_auto_validar_forms/listar.html', {'listar': listar})