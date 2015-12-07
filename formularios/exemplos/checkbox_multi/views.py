from django.shortcuts import render, get_object_or_404, redirect
from checkbox_multi.models import Transportes

def index(request):
    return render(request, 'checkbox_multi/index.html', {})
    
def enviar(request):
    if request.method == 'POST':
        transportes = Transportes.objects.create(
            opcoes_transp = request.POST.getlist('opcoes_transp','Nenhuma opção foi escolhida')
        )
        
    return redirect('checkbox_multi:checkbox_multi.views.listar')
       
       
def listar(request):
    transportes = Transportes.objects.order_by('-id')
    return render(request, 'checkbox_multi/listar.html', {'transportes':transportes})


def carregar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    return render(request, 'checkbox_multi/ver-alternativas.html', {'transporte': transporte})


def atualizar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    if request.method == 'POST':
        opcoes_transp = request.POST.getlist('opcoes_transp','Nenhuma opção foi escolhida')
                
        transporte.opcoes_transp = opcoes_transp
        transporte.save()
        
    return render(request, 'checkbox_multi/ver-alternativas.html', {'transporte': transporte})
        
def deletar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    transporte.delete()
    
    return redirect('checkbox_multi:checkbox_multi.views.listar')