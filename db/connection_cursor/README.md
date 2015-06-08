Connection & Cursor
===

Neste exemplo é mostrado como utilizar o Cursor do Django para executar as query SQL diretamente sem a necessidade de se 
utilizar uma model para inserir, editar, deletar e ver registros (CRUD).

A classe sql.py contém as funções de manipulação de dados do banco de dados onde:

. def dict_convert(row, x):

    Recebe o resultado do SQL em um array e converte para um Dicionário.

. slq_select(campos, tabela, criterio):

    Recebe os nomes de quais campos da tabela serão mostrados, o nome da tabela que será manipulada e os critérios de 
    busca caso necessário, seu resultado é uma lista de dicionário contendo os registros encontrados de acordo com os 
    critérios selecionados.

. sql_insert(tabela, campos, dados)

    Recebe o nome da tabela que será manipulada, quais os campos que serão adicionados e os valores de cada dados adicionado, 
    ao receber todos os parâmetros é inserido um novo registro no bando de dados.

. sql_update(tabela, campos, pk)

    Recebe o nome da tabela que será manipulada, quais os campos e suas alterações que serão atualizadas e o id do registro 
    que será alterado, ao receber todos os parâmetros o registro é atualizado. 
    
. sql_delete(tabela, pk)

    Recebe o nome da tabela que será manipulada e o id do registro que será removido, ao receber todos os parâmetro o 
    registro é removido do banco de dados.


Para manipular os registros do banco de dados pelo Shell do Django clique no link abaixo:
[Manipulando registros no banco de dados pelo Shell](manipulando-registros-shell/README.md)