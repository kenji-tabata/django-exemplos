Criando Modelos (ou criando apps?)
===

Aqui ampliamos discussão ["Projects vs. apps"](projects-vs-apps.md) para "modelos ou apps ?".

Mas, independente desse entendimento, vamos colocar a mão na massa...

Considerando os passos dos artigos anteriores, podemos criar uma app em seu projeto.

Vá até o seu  projeto, ex: `cd /projetos/mysite` e crie um novo modelo chamado `polls` (veja o significado de 
[poll](https://translate.google.com.br/?hl=pt-BR&authuser=0#en/pt/poll)).

O comando abaixo cria uma nova app em seu projeto.

    $ python3 manage.py startapp polls

Ele criará a seguinte estrutura de diretórios.

    polls/
        __init__.py
        admin.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py

E, portanto, nosso projeto ficará dessa forma....

    /mysite/
        /mysite/
        /polls/




Definindo o modelo
---        

Vamos alterar o conteúdo do arquivo `/mysite/polls/models.py` conforme o exibido abaixo.

    from django.db import models

    class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')

    class Choice(models.Model):
        question = models.ForeignKey(Question)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)    

Leia a documentação para saber mais detalhes.




Ativando o Modelo
---

Altere o arquivo `mysite/settings.py` para incluir sua app.

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'polls',
    )


Precisamos avisar ao Django para incluir a app, execute o comando abaixo.

    $ python3 manage.py makemigrations polls

Após isso, não é obrigatório, mas você pode checar se seu modelo está OK.

    $ python3 manage.py check

E também pode quere ver o SQL gerado.    

    $ python3 manage.py sqlmigrate polls 0001


Se tudo OK, podemos então criar as tabelas necessáris em nosso banco de dados com o comando abaixo.

    $ python3 manage.py migrate    


Migrações (migrations) é um recurso que auxila o desenvolvimento no tocante as alterações realizadas no banco de dados.
Você pode deletar, criar ou alterar tabelas, ou seja, manipular seu banco de dados através do Django, quer dizer, sem 
ter que mexer na interface do DB.


###  Organizando o processo...

- Altere seus modelos.
- Execute `python3 manage.py makemigrations` para criar migrações de suas alterações.
- Execute `python3 manage.py migrate` para efetuar as alterações no banco de dados.
