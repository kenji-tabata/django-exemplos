from django.shortcuts import render
from lista_filtro.models import Usuario
from django.template import Context, Template

def index(request):
    list_user = Usuario.objects.all()
    html = cabecalho('#asc', '', '', 'ordem_asc')
    
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

def order_by_asc(request, tipo):
    html = cabecalho('#desc', 'Asc', tipo, 'ordem_desc')
    
    list_user = Usuario.objects.order_by(tipo)
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

def order_by_desc(request, tipo):
    html = cabecalho('#', 'Desc', tipo, 'ordem_ult')

    list_user = Usuario.objects.order_by('-'+tipo)
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})
        
def order_by_ult(request, tipo):
    list_user = Usuario.objects.order_by('-id')
    html = cabecalho('#asc', '', '', 'ordem_asc')
    
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

'''
    Cria o cabeçalho da tabela com a opção de fitragem de dados
    A função altera a listagem sem a utilização do Ajax
'''
def cabecalho(link, ordem, tipo, url):
    tipos = ('id', 'nome', 'email', 'data', 'status')
    
    tabHeader =''

    for titulo in tipos:
        if titulo == tipo:
            print (link)
            tabHeader += ("<th><a href='/%s/%s%s' title='%s' id='%s'>%s %s</a></th>" % (url, titulo, link, titulo, titulo, titulo.lower().capitalize(), ordem))
        else:
            tabHeader += ("<th><a href='/ordem_asc/%s#asc' title='%s' id='%s'>%s</a></th>" % (titulo, titulo, titulo, titulo.lower().capitalize()))
        
    titulos = Template(tabHeader)
    
    context = Context({'ordem': ordem})
    
    return titulos.render(context)