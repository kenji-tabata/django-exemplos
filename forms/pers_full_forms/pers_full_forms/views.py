from django.shortcuts import render
from pers_full_forms.forms import FormularioForm
from django.shortcuts import redirect
from pers_full_forms.models import Formulario

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pers_full_forms.views.listar')
    else:
        form = FormularioForm()
    return render(request, 'pers_full_forms/index.html', {'form': form})

def listar(request):
    listar = Formulario.objects.order_by('-id')
    return render(request, 'pers_full_forms/listar.html', {'listar': listar})