from django.shortcuts import render
from lista_filtro.models import Usuario
from django.template import Context, Template

def index(request):
    list_user = Usuario.objects.all()
    html = cabecalho('#asc', '', '')
    
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

def order_by_asc(request):
    tipo = request.GET.get('tipo')
    html = cabecalho('#desc', 'Asc', tipo)
    
    list_user = Usuario.objects.order_by(tipo)
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

def order_by_desc(request):
    tipo = request.GET.get('tipo')
    html = cabecalho('#', 'Desc', tipo)

    list_user = Usuario.objects.order_by('-'+tipo)
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})
        
def order_by_ult(request):
    list_user = Usuario.objects.order_by('-id')
    html = cabecalho('#', '', '')
    
    return render(request, 'lista_filtro/index.html', {'list_user': list_user, 'html': html})

'''
    Cria o cabeçalho da tabela com a opção de fitragem de dados 
'''
def cabecalho(link, ordem, tipo):
    tipos = ('id', 'nome', 'email', 'data', 'status')
    
    tabHeader =''
    
    for titulo in tipos:
        if titulo == tipo:
            tabHeader += ("<th><a href='%s' title='%s' id='%s'>%s %s</a></th>" % (link, titulo, titulo, titulo.lower().capitalize(), ordem))
        else:
            tabHeader += ("<th><a href='#asc' title='%s' id='%s'>%s</a></th>" % (titulo, titulo, titulo.lower().capitalize()))
        
    titulos = Template(tabHeader)
    
    context = Context({'link': link, 'ordem': ordem})
    
    return titulos.render(context)