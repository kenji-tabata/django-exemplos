Listagem com filtro de ordenação sem Ajax
===

Neste exemplo é mostrado como ordenar uma lista de uma tabela ao clicar no nome da coluna utilizando somente o Django. 
O Javascript do `lista_filtro_com_ajax` foi adaptado para funcionar neste exemplo também e está comentado. 

Quando o Ajax estiver desabilitado o Django faz as requisições e atualiza a tabela quando clicar no link do cabeçalho, a 
principal diferença ao utilizar o Ajax aparece na verificação da url e no envio da url pelo get.

O Ajax quando habilitado fica encarregado de encaminhar para a url de acordo com o critério escolhido (#asc, #desc ou #ult) 
e atualizar a tabela. O Django realiza a ordenação e pela troca do cabeçalho da tabela com os links correspondentes.
