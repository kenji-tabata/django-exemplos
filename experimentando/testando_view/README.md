12. Testando a VIEW no Shell do Python
===

Inicie o Shell do projeto

    python manage.py shell


Para todos os exemplos de testes com request utilize o código abaixo para importar o teste do cliente

    >>> from django.test import Client
    >>> c = Client()

Testando index

    >>> resp = c.get('')
    Listar todos os contatos

Testando formulário para adicionar contato

    >>> resp = c.get('/adicionar/')
    Adicionar Contato

Testando o envio do formulário de contato

    >>> resp = c.post('/enviar/', {'nome': 'Carlos', 'email': 'email@mail.com', 'data': '2015-04-01 12:00:00', 'mensagem': 'Testando o envio do formulário'})
    Contanto de Carlos foi adicionado com sucesso

    >>> resp = c.post('/enviar/')
    Erro: Não preencheu todos os campos

Testando o editar do formulário de contato

    >>> resp = c.post('/editar/18/', {'nome': 'Carlos Henrique', 'email': 'email@mail.com', 'data': '2015-04-01 17:30:00', 'mensagem': 'Testando o envio do formulário'})
    Contanto de Carlos Henrique foi alterado com sucesso

    resp = c.post('/editar/18/')
    Erro: Não preencheu todos os campos


Testando a visualização dos detalhes do contato

    >>> resp = c.get('/detalhes/18/')
    Ver detalhes do contato Carlos

Testando o excluir contato

    >>> resp = c.get('/deletar/19/')
    O Contato João Silveira foi deletado.


