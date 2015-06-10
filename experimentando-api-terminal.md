Experimentando a API (Playing with the API)
===

Criamos o projeto, criamos e migramos os modelos, agora que tal experimentarmos isso no terminal?

É o que vamos fazer, para abrirmos o terminal com o apoio das variáveis do projeto executamos...

    $ python3 manage.py shell


Ou, se preferir, execute...

    $ python3
    >>> import django
    >>> django.setup()


### Início

Importe os modelos que você precisar.

    >>> from polls.models import Question, Choice

Possuímos alguns registros?

    >>> Question.objects.all()
    []

Vamos criar uma nova questão (question).

    >>> from django.utils import timezone
    >>> q = Question(question_text="What's new?", pub_date=timezone.now())


Salve o objeto no banco.
    
    >>> q.save()

Vamos consultar o id do objeto?

    >>> q.id
    1

Podemos consultar outras propriedades.

    >>> q.question_text
    "What's new?"

    >>> q.pub_date
    datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

Se alteramos alguma coisa, não podemos esquecer de persistir o objeto.

    >>> q.question_text = "What's up?"
    >>> q.save()


### \_\_str\_\_

E agora, como está nossa tabela?

    >>> Question.objects.all()
    [<Question: Question object>]

Essa não é uma boa representação de nossos objetos, para melhorarmos isso vamos alterar o arquivo `/mysite/polls/models.py`
conforme o conteúdo abaixo (repare que parte do conteúdo já existente deve permanecer).

    from django.db import models

    class Question(models.Model):
        # ...
        def __str__(self):
            return self.question_text

    class Choice(models.Model):
        # ...
        def __str__(self):
            return self.choice_text

Vamos aproveitar e incluir o seguinte trecho ao arquivo.

    import datetime

    from django.db import models
    from django.utils import timezone

    class Question(models.Model):
        # ...
        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


Agora, retornemos ao terminal `python3 manage.py shell`.

Como iniciamos nova seção, devemos incluir novamente os modelos.

    >>> from polls.models import Question, Choice

Vamos testar nossa função `__str__()`?

    >>> Question.objects.all()
    [<Question: What's up?>]

Também podemos filtrar o conteúdo através da API, por exemplo...

    >>> Question.objects.filter(id=1)
    [<Question: What's up?>]

    >>> Question.objects.filter(question_text__startswith='What')
    [<Question: What's up?>]

    >>> from django.utils import timezone
    >>> current_year = timezone.now().year
    >>> Question.objects.get(pub_date__year=current_year)
    <Question: What's up?>

Se consultarmos um id que não existe...

    >>> Question.objects.get(id=2)
    Traceback (most recent call last):
        ...
    DoesNotExist: Question matching query does not exist.


É comum procurarmos pela chave primária, o Django fornece um atalho...

    >>> Question.objects.get(pk=1)
    <Question: What's up?>

... que é semelhante a linha abaixo.

    >>> Question.objects.get(id=1).
    <Question: What's up?>

Vamos testar o método `was_published_recently()`?

    >>> q = Question.objects.get(pk=1)
    >>> q.was_published_recently()
    True



### Chave estrangeira

Você deve ter o entendimento de relacionamento de chave estrangeira.

A chamada construtora...

    >>> q = Question.objects.get(pk=1)

- cria um novo objeto Choice, 
- faz a instrução `INSERT`,
- adiciona uma choice (escolha) para o conjunto de chopices (escolhas) relacionadas e
- retorna um novo objeto Choice.

Então será que temos choices (escolhas) relacionadas?

    >>> q.choice_set.all()
    []

Não! Então vamos criar algumas.

    >>> choice1 = q.choice_set.create(choice_text='Not much', votes=0)
    >>> choice2 = q.choice_set.create(choice_text='The sky', votes=0)
    >>> choice3 = q.choice_set.create(choice_text='Just hacking again', votes=0)

Repare que o objeto Choice possui uma API de acesso para suas Questions (questões) relacionadas...
    
    >>> choice3.question
    <Question: What's up?>

... e vice versa. O objeto Question também possui acesso aos Objetos Choice.
    
    >>> q.choice_set.all()
    [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]
    
    >>> q.choice_set.count()
    3

A API, automaticamente, segue os relacionamentos que você precisa.

Use sublinhados dupĺos (double underscores) para separar relacionamentos.
Isto funciona para quantos níveis de profundidade que você precisar; não há limite.
Encontre todas  Choices (escolhas) para qualquer questão cujo `pub_date` seja o ano atual.
(reutilizamos a vairável `current_year` que criamos anteriormente)

    >>> Choice.objects.filter(question__pub_date__year=current_year)
    [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]


### Delete

Para deletar um das choices (escolhas) use `delete()`.

    >>> c = q.choice_set.filter(choice_text__startswith='Just hacking')
    >>> c.delete()