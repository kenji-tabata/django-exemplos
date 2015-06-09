Performing raw SQL queries
===

Neste exemplo é mostrado como utilizar os comando SQL puros para fazer consultas, filtrar registros, buscar registros e 
utilizar o INNER JOIN do SQL. O Raw SQL é utilizado somente para consultas simples, ele não permite inserir, deletar ou 
editar registros, para utilizar as funções do CRUD utilize o Cursor ou o Django ORM.


Considerando o seguinte modelo.

    class Person(models.Model):
        first_name = models.CharField(...)
        last_name = models.CharField(...)
        birth_date = models.DateField(...)

Podemos recuperar os reguistros da seguinte forma:

    for p in Person.objects.raw('SELECT * FROM myapp_person'):
        print(p)

Veja a [documentação](https://docs.djangoproject.com/en/1.8/topics/db/sql/).


Dentro de uma view fazemos dessa forma:

    def index(reponse):
        person = Person.objects.raw('SELECT * FROM myapp_person')
        return render(request, 'myapp/index.html', {'persons': person})

E o template seria semalhante a isto...


    {% for person in persons %}
        <p>Nome: {{ person.nome }}</p>
    {% endfor %}        


