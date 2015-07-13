from django.shortcuts import render, get_object_or_404, redirect
from testando_template.models import Contato
from testando_template.forms import ContatoForm

def index(request):
    contatos = Contato.objects.order_by('-id')
    print('Listar todos os contatos')
    return render(request, 'testando_template/index.html', {'contatos': contatos})


def adicionar(request):
    form = ContatoForm()
    print('Adicionar Contato')
    return render(request, 'testando_template/adicionar.html', {'form': form})


def enviar(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            contato = form.save()
            print('Contanto de '+contato.nome+' foi adicionado com sucesso')
            return redirect('testando_template.views.detalhes', pk=contato.pk) 
        else:
            print('Erro: Não preencheu todos os dados')
    else:
        form = ContatoForm()
        print('Formulário de contato enviado pelo método GET')
        
    return render(request, 'testando_template/adicionar.html', {'form': form})        


def editar(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            contato.save()
            print('Contanto de '+contato.nome+' foi alterado com sucesso')
            return redirect('testando_template.views.detalhes', pk=contato.pk) 
        else:
            print('Erro: Não preencheu todos os campos')
    else:
        form = ContatoForm(instance=contato)
        print('Formulário de contato enviado pelo método GET')
        
    return render(request, 'testando_template/editar.html', {'form': form})        

def deletar(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    
    if contato:
        print('O Contato '+contato.nome+' foi deletado.')
        contato.delete()
    else:
        print('Contato não encontrado')
        
    return redirect('testando_template.views.index')

def detalhes(request, pk):
    contato = get_object_or_404(Contato, pk=pk)
    
    if contato:
        print('Ver detalhes do contato '+contato.nome)
    else:
        print('Contato não encontrado')
        
    return render(request, 'testando_template/detalhes.html', {'contato': contato})
