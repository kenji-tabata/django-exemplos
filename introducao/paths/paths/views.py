from django.shortcuts import render
from django.conf import settings

def index(request):
    arquivo = open('%s/texto.txt' % settings.NOVA_PASTA)

    if arquivo:
        texto = arquivo.read()
        arquivo.close()
    
    arq_links = open('%s/README.md' % settings.PASTA_LINKS)
    
    if arq_links:
        texto2 = arq_links.read()
        arq_links.close()
    
    return render(request, 'paths/index.html', {'texto': texto, 'texto2': texto2})
