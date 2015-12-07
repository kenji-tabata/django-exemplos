Relacionamento Many to Many (muitos para muitos) com tabela intermediária
===

No model abaixo a classe Membership é a classe intermediária que faz a ligação com as classes
Person e Group.

```python
from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)
```

Na classe Group é adicionada o campo `members` como many-to-many para associar o Person com o Group
na classe intermediária.

Adicionando registro:

```python
# Adicione primeiro o Person e o Group...
ringo = Person.objects.create(name="Ringo Starr")
paul = Person.objects.create(name="Paul McCartney")
beatles = Group.objects.create(name="The Beatles")

# Para depois adicionar o relacionamento entre eles
m1 = Membership(person=ringo, group=beatles,
    date_joined=date(1962, 8, 16),
    invite_reason="Needed a new drummer.")
m1.save()
```

Visualizando registros:

```python
# Todos os registros do group
beatles.members.all()

# Todos os registros do person
ringo.group_set.all()

# Registros que começam com Paul
Group.objects.filter(members__name__startswith='Paul')

# Um registro especifico
Person.objects.get(group__name='The Beatles', membership__date_joined__gt=date(1961,1,1))

# Visualizar somente os dados da tabela intermediária
ringos_membership = Membership.objects.get(group=beatles, person=ringo)
ringos_membership.date_joined
```