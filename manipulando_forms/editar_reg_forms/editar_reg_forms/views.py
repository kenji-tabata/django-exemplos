from django.shortcuts import render, get_object_or_404, redirect
from editar_reg_forms.forms import FormularioForm
from editar_reg_forms.models import Formulario

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('editar_reg_forms.views.listar')
    else:
        form = FormularioForm()
        
    return render(request, 'editar_reg_forms/index.html', {'form': form})


def listar(request):
    listar = Formulario.objects.order_by('-id')
    return render(request, 'editar_reg_forms/listar.html', {'listar': listar})

def editar(request, pk):
    formulario = get_object_or_404(Formulario, pk=pk)
    if request.method == "POST":
        form = FormularioForm(request.POST, instance=formulario)
        if form.is_valid():
            formulario.save()
            return redirect('editar_reg_forms.views.listar') 
        
    else:
        form = FormularioForm(instance=formulario)
        
    return render(request, 'editar_reg_forms/index.html', {'form': form})        