Raw Query
===

Neste exemplo é mostrado como utilizar os comando SQL puros para fazer consultas, filtrar registros, buscar registros e 
utilizar o INNER JOIN do SQL. O Raw SQL é utilizado somente para consultas simples, ele não permite inserir, deletar ou 
editar registros, para utilizar as funções do CRUD utilize o Cursor ou o Django ORM.

Abaixo estão os comando SQLs realizados por cada função:

    Função              Comando SQL
    select_all():       'SELECT * FROM raw_query_usuario'
    select_id           'SELECT * FROM raw_query_usuario WHERE id = %s', [pk]
    select_translation  'SELECT nome AS nome_completo, email AS email_pessoal, pk AS id FROM raw_query_usuario'
    select_first        'SELECT * FROM raw_query_usuario LIMIT 1'
    select_filter       'SELECT * FROM raw_query_usuario WHERE id BETWEEN 1 AND 2'
    select_order_desc   'SELECT * FROM raw_query_usuario ORDER BY nome DESC'
    select_like         'SELECT * FROM raw_query_usuario WHERE nome LIKE %s', ['%'+nome+'%']
    select_inner_join   '''SELECT * FROM raw_query_usuario 
                           INNER JOIN raw_query_comentario 
                           ON raw_query_usuario.id = raw_query_comentario.usuario_id'''


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


        <p><a href="{% url 'mostrar_todos' %}">Mostrar todos</a></p>
        <p><a href="{% url 'mostrar_pelo_id' pk=3 %}">Mostrar por id</a></p>
        <p><a href="{% url 'mostrar_translation' %}">Mostrar com translations</a></p>
        <p><a href="{% url 'mostrar_primeiro' %}">Mostrar primeiro registro</a></p>
        <p><a href="{% url 'mostrar_filtro' %}">Mostrar com filtro</a></p>
        <p><a href="{% url 'mostrar_ordem_desc' %}">Mostrar por ordem de nome decrescente</a></p>
        <p><a href="{% url 'mostrar_like' nome='Caio' %}">Mostrar com LIKE</a></p>
        <p><a href="{% url 'mostrar_todos_inner_join' %}">Mostrar todos com INNER JOIN</a></p><br>                                        