Links

Neste exemplo é mostrado como criar links para acessar as outras páginas do site.

Existem 2 métodos para colocar um link em um template:

1. Hardcoded URL:

    <a href="/enquetes/">Enquetes</a>

2. Template TAG:

    <a href="{% url 'enquetes' %}">Enquetes</a>


Para o Template TAG encontrar qual URL está sendo requisitada utilizamos o valor do atributo `name` da URL (urls.py):

    url(r'^enquetes$', views.ver_enquetes, name='enquetes'),

Também podemos fazer a requisição ao chamar a VIEW diretamente ao invés do atributo `name`:

    <a href="{% url 'views.ver_enquetes' %}">Enquetes</a>

Ao chamar a VIEW ao invés do nome podemos deixar mais implícito sobre da onde a URL está sendo requisitada, caso ela vir 
de outra aplicação por exemplo:

    <a href="{% url 'enquete.views.ver_enquetes' %}">Enquetes</a>

No caso acima a função ver_enquetes está no módulo VIEWS da aplicação Enquete.