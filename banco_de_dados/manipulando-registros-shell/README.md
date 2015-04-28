Manipulando registros no banco de dados pelo Shell
===

Exemplo para tabela de Usuário (com Primary Key)
---

### Inserindo um registro de usuários

    >>> from connection_cursor.models import Usuario
    >>> Usuario.objects.create(nome='Qualquer Nome', email='qualquer@mail.com')


### Listando todos os registros de usuários

    >>> Usuario.objects.all()

### Selecionando apenas um registro de usuário

    >>> u = Usuario.objects.get(id=1)

### Removendo registros de usuários

Para deletar apenas um usuário digite:

    >>> u = Usuario.objects.get(id=2)
    >>> u.delete()

Para deletar todos os usuários digite:

    >>> u = Usuario.objects.all()
    >>> u.delete()



Exemplo para a tabela do Comentário (com ForeignKey do Usuário)
---

### Inserindo um comentário para o usuário

    >>> from connection_cursor.models import Usuario
    >>> from connection_cursor.models import Comentario

    >>> u = Usuario.objects.get(id=1)
    >>> u.comentario_set.create(mensagem="Testando mensagem")

### Listando todos os comentários do usuário

    >>> u = Usuario.objects.get(id=1)
    >>> u.comentario_set.all()

### Removendo registros do comentário

Para deletar um comentário do usuário digite:

    >>> c = u.comentario_set.get(id=1)
    >>> c.delete()

Para deletar todos os comentários do usuário digite:

    >>> c = u.comentario_set.all()
    >>> c.delete()