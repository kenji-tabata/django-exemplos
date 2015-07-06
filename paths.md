Paths
===

- Pasta raiz do projeto:

    os.path.dirname(os.path.dirname(__file__)) 

- Pasta dentro da raiz do projeto:

    os.path.join(BASE_DIR, 'templates')
    os.path.join(BASE_DIR, 'nova_pasta')
    
O `os.path.join` irá concatenar o caminho da pasta raiz com o nome da pasta.

- Pasta que está fora da pasta raiz do projeto (um nível acima):

    os.path.join(os.path.dirname(BASE_DIR), 'links')

O `os.path.dirname(BASE_DIR)` irá voltar uma pasta acima do projeto.



