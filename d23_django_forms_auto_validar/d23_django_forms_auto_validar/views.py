from django.shortcuts import render
from django.shortcuts import redirect
from d23_django_forms_auto_validar.forms import FormularioForm
from d23_django_forms_auto_validar.models import Formulario

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('d23_django_forms_auto_validar.views.listar')
    else:
        form = FormularioForm()
        
    return render(request, 'd23_django_forms_auto_validar/index.html', {'form': form})


def listar(request):
    listar = Formulario.objects.order_by('-id')
    return render(request, 'd23_django_forms_auto_validar/listar.html', {'listar': listar})