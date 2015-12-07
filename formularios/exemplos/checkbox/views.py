from django.shortcuts import render, get_object_or_404, redirect
from checkbox.models import Transportes

def index(request):
    return render(request, 'checkbox/index.html', {})
    
def enviar(request):
    if request.method == 'POST':
        
        p_carro = request.POST.get('carro','Não')
        p_moto = request.POST.get('moto','Não')
        p_onibus = request.POST.get('onibus','Não')
        p_bicicleta = request.POST.get('bicicleta','Não')

        transportes = Transportes.objects.create(
            carro = p_carro,
            moto = p_moto,
            onibus = p_onibus,
            bicicleta = p_bicicleta,
        )
        
    return redirect('checkbox:checkbox.views.listar')
       
       
def listar(request):
    transportes = Transportes.objects.order_by('-id')
    return render(request, 'checkbox/listar.html', {'transportes':transportes})


def carregar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    return render(request, 'checkbox/ver-alternativas.html', {'transporte': transporte})


def atualizar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    if request.method == 'POST':
        p_carro = request.POST.get('carro','Não')
        p_moto = request.POST.get('moto','Não')
        p_onibus = request.POST.get('onibus','Não')
        p_bicicleta = request.POST.get('bicicleta','Não')
                
        transporte.carro = p_carro
        transporte.moto = p_moto
        transporte.onibus = p_onibus
        transporte.bicicleta = p_bicicleta 
        transporte.save()
        
    return render(request, 'checkbox/ver-alternativas.html', {'transporte': transporte})
        
def deletar(request, pk):
    transporte = get_object_or_404(Transportes, pk=pk)
    
    transporte.delete()
    
    return redirect('checkbox:checkbox.views.listar')