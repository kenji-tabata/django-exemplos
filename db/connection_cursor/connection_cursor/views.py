from django.shortcuts import render, redirect
from connection_cursor.sql import SQL

def index(request):
    return render(request, 'connection_cursor/index.html', {})

def select_all(request):
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario','')
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})

def select_id(request, pk):
    criterio = "WHERE id = %s" % (pk)
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario', criterio)
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})
    
def select_first(request):
    criterio = 'LIMIT 1'
    usuario = SQL.slq_select('*', 'connection_cursor_usuario', criterio)[0]
    return render(request, 'connection_cursor/index.html', {'usuario': usuario})

def select_filter(request):
    criterio = 'WHERE id BETWEEN 1 AND 2'
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario', criterio)
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})

def select_order_desc(request):
    criterio = 'ORDER BY id DESC'
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario', criterio)
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})

def select_like(request, nome):
    criterio = "WHERE nome LIKE '%s'" % ('%'+nome+'%')
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario', criterio )
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})
    
def select_inner_join(request):
    criterio = '''INNER JOIN connection_cursor_comentario 
                  ON connection_cursor_usuario.id = connection_cursor_comentario.usuario_id'''
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario', criterio)
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})

def select_combined(request):
    criterios = 'INNER JOIN connection_cursor_comentario ON usuario.id = connection_cursor_comentario.usuario_id '
    criterios += 'WHERE usuario.id BETWEEN 1 AND 2 '
    criterios += 'ORDER BY id DESC'
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario AS usuario', criterios)
    return render(request, 'connection_cursor/index.html', {'usuarios': usuarios})

def insert_usuario(request):
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
        
        dados = "'%s','%s'" % (nome, email)
        
        SQL.sql_insert("connection_cursor_usuario","nome, email", dados)
    
    return redirect('connection_cursor.views.select_all')

def insert_comentario(request):
    if request.method == 'POST':
        usuario_id = request.POST['usuario_id']
        mensagem = request.POST['mensagem']
        
        dados = "'%s','%s'" % (usuario_id, mensagem)
        
        SQL.sql_insert("connection_cursor_comentario","usuario_id, mensagem", dados)
    
    return redirect('connection_cursor.views.select_inner_join')

def update_usuario(request, pk):
    criterio = "WHERE id = %s" % (pk)
    usuarios = SQL.slq_select('*', 'connection_cursor_usuario', criterio)
    
    if request.method == 'POST':
        nome = request.POST['nome']
        email = request.POST['email']
            
        dados = "nome = '%s', email = '%s'" % (nome, email)
        SQL.sql_update("connection_cursor_usuario", dados, pk )
    
        return redirect('connection_cursor.views.select_all')
            
    return render(request, 'connection_cursor/detalhes.html', {'usuarios': usuarios})

    
def delete_usuario(request, pk):
    if pk:
        SQL.sql_delete("connection_cursor_usuario", pk)
        
    return redirect('connection_cursor.views.select_all')
    
    