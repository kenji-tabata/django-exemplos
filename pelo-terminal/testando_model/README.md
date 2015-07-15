Testando o Model no Shell do Python
===

Inicie o Shell do projeto

    python manage.py shell

Importe o model do projeto

    >>> from testando_model.models import Contato



Ver todos os registros cadastrados

    >>> Contato.objects.all()

Inserindo um registro

    >>> from django.utils import timezone
    >>> c = Contato(nome='Lucas', email='lucas@mail.com', data=timezone.now(), mensagem='Mensage de teste' )
    >>> c.save()

Carregar um registro especifico como objeto

    >>> c = Contato.objects.get(id=1)

Ver qual registro o objeto esta carregando

    >>> c.id

Alterando um valor do registro

    >>> c.nome = "novo-nome"
    >>> c.save()

Visualizar um dado especifico do registro

    >>> c.nome
    >>> Contato.objects.get(id=2).data

Filtrar os registros

    >>> Contato.objects.filter(id=1)

Deletar um registro

    >>> c.delete()