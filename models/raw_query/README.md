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



Para manipular os registros do banco de dados pelo Shell do Django clique no link abaixo:
[Manipulando registros no banco de dados pelo Shell](manipulando-registros-shell/README.md)