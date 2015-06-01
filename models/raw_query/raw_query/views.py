from django.shortcuts import render
from raw_query.models import Usuario

def index(request):
    return render(request, 'raw_query/index.html', {})

def select_all(request):
    usuarios = Usuario.objects.raw('SELECT * FROM raw_query_usuario')
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})

def select_id(request, pk):
    usuarios = Usuario.objects.raw('SELECT * FROM raw_query_usuario WHERE id = %s', [pk])
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})
    
def select_translation(request):
    map = {'nome': 'nome_completo', 'email': 'email_pessoal', 'pk': 'id'}
    usuarios = Usuario.objects.raw('SELECT * FROM raw_query_usuario', translations=map)
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})
    
def select_first(request):
    usuario = Usuario.objects.raw('SELECT * FROM raw_query_usuario LIMIT 1')[0]
    return render(request, 'raw_query/index.html', {'usuario': usuario})

def select_filter(request):
    usuarios = Usuario.objects.raw('SELECT * FROM raw_query_usuario WHERE id BETWEEN 1 AND 2')
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})

def select_order_desc(request):
    usuarios = Usuario.objects.raw('SELECT * FROM raw_query_usuario ORDER BY nome DESC')
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})

def select_like(request, nome):
    usuarios = Usuario.objects.raw("SELECT * FROM raw_query_usuario WHERE nome LIKE '%s'" % ('%'+nome+'%'))
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})
    
def select_inner_join(request):
    usuarios = Usuario.objects.raw('''SELECT * FROM raw_query_usuario 
                                        INNER JOIN raw_query_comentario 
                                        ON raw_query_usuario.id = raw_query_comentario.usuario_id''')
    return render(request, 'raw_query/index.html', {'usuarios': usuarios})

