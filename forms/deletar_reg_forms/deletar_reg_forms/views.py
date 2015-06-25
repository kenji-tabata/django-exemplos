from django.shortcuts import render, get_object_or_404, redirect
from deletar_reg_forms.forms import FormularioForm
from deletar_reg_forms.models import Formulario

def index(request):
    if request.method == "POST":
        form = FormularioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('deletar_reg_forms.views.listar')
    else:
        form = FormularioForm()
        
    return render(request, 'deletar_reg_forms/index.html', {'form': form})


def listar(request):
    listar = Formulario.objects.order_by('-id')
    return render(request, 'deletar_reg_forms/listar.html', {'listar': listar})

def deletar(request, pk):
    formulario = get_object_or_404(Formulario, pk=pk)
    
    if formulario:
        formulario.delete()
    
    return redirect('deletar_reg_forms.views.listar')
