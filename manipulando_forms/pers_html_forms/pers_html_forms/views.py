from django.shortcuts import render
from pers_html_forms.forms import FormularioForm
from django.shortcuts import redirect
from pers_html_forms.models import Formulario

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pers_html_forms.views.listar')
    else:
        form = FormularioForm()
    return render(request, 'pers_html_forms/index.html', {'form': form})

def listar(request):
    listar = Formulario.objects.order_by('-id')
    return render(request, 'pers_html_forms/listar.html', {'listar': listar})