from django.shortcuts import render
from manipulando_arquivos.arquivo import Arquivo

def index(request):    
    return render(request, 'manipulando_arquivos/index.html', {})
   
    
def criar_arquivo(request):
    if request.method == 'POST':
        nome_arquivo = request.POST['nome']
        conteudo = request.POST['conteudo']
        if nome_arquivo !="":
            nome_arquivo += ".txt"
        
        arquivo = Arquivo()
        
        operacao = arquivo.criar_arquivo(nome_arquivo, conteudo)
                
        return render(request, 'manipulando_arquivos/index.html', {'arquivo': operacao})
    
    elif request.method == 'GET':
        return render(request, 'manipulando_arquivos/criar.html', {})
       
        
def ler_arquivo(request, tipo):
    arquivo = Arquivo()
    html = arquivo.combobox_arquivos()
    
    if request.method == 'POST':
        nome_arquivo = request.POST['nome']
        
        arquivo = Arquivo()
        
        operacao = arquivo.ler_arquivo(nome_arquivo)
        
        if tipo == 'leitura':
            return render(request, 'manipulando_arquivos/ler.html', {'html': html, 'leitura': operacao,'nome_arquivo': nome_arquivo})
        elif tipo == 'edicao':
            return render(request, 'manipulando_arquivos/editar.html', {'html': html, 'editar': operacao,'nome_arquivo': nome_arquivo})
        elif tipo == 'adicao':
            return render(request, 'manipulando_arquivos/adicao.html', {'html': html, 'nome_atual': nome_arquivo})
        elif tipo == 'deletar':
            return render(request, 'manipulando_arquivos/deletar.html', {'html': html, 'nome_atual': nome_arquivo})
        else:
            return render(request, 'manipulando_arquivos/index.html', {'html': html})
    
    elif request.method == 'GET':
        if tipo == 'leitura':
            return render(request, 'manipulando_arquivos/ler.html', {'html': html})
        elif tipo == 'edicao':
            return render(request, 'manipulando_arquivos/editar.html', {'html': html})
        elif tipo == 'adicao':
            return render(request, 'manipulando_arquivos/adicao.html', {'html': html})
        elif tipo == 'deletar':
            return render(request, 'manipulando_arquivos/deletar.html', {'html': html})
        else:
            return render(request, 'manipulando_arquivos/index.html', {'html': html})
        
            
def salvar_arquivo(request, tipo):
    if request.method == 'POST':
        nome_arquivo = request.POST['nome']
        conteudo = request.POST['conteudo']
        
        arquivo = Arquivo()
        
        if tipo == 'edicao':
            operacao = arquivo.salvar_arquivo(nome_arquivo, conteudo)
        
        elif tipo == 'adicao':
            operacao = arquivo.adicionar_conteudo(nome_arquivo, conteudo)
                
        return render(request, 'manipulando_arquivos/index.html', {'arquivo': operacao})
    
    elif request.method == 'GET':
        return render(request, 'manipulando_arquivos/index.html', {})
    
    
def deletar_arquivo(request):
    if request.method == 'POST':
        nome_arquivo = request.POST['nome']
        
        arquivo = Arquivo()
        
        operacao = arquivo.deletar_arquivo(nome_arquivo)
        
        return render(request, 'manipulando_arquivos/index.html', {'arquivo': operacao})
    
    elif request.method == 'GET':
        return render(request, 'manipulando_arquivos/index.html', {})    
    