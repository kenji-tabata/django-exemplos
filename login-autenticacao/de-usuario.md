Autenticação de Usuário no Django
===

https://docs.djangoproject.com/en/dev/topics/auth/

Django possui um sistema de autenticação de usuário.

Para instalar é preciso habilitar as apps listadas abaixo:

- django.contrib.auth
- django.contrib.contenttypes'

...e também os middle ware listados abaixo:

- django.contrib.sessions.middleware.SessionMiddleware
- django.contrib.auth.middleware.AuthenticationMiddleware


Por padrão, a configuração requerida já vem incluída no arquivo `settings.py` gerado pelo comando `django-admin startproject`.

    # settings.py
    ...
    ...
    ...
    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',         # <---- olha eles aqui
        'django.contrib.contenttypes', # <---- olha eles aqui
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles'
    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',             # <---- olha eles aqui
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',          # <---- olha eles aqui
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware'
    )
    ...
    ...
    ...


### Objetos User¶

O objeto `User` é o *core* do sistema de autenticação.

Há uma única classe de usuários dentro do Django que representa, por exemplo: superusers (ou admin) e os demais usuários
de seus sistema (staff users).


### Criando um usuário comum

Para acessar o seu projeto pelo terminal, lembre-se, o comando é `$ python manage.py shell`.

Para experimentar a sequencia de comandos abaixo você deve ter o seu projeto devidamente instalado e inicializado (
execute o *migrate*).

    >>> from django.contrib.auth.models import User
    >>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    >>> user.last_name = 'Lennon'
    >>> user.save()


### Criando um super usuário (superusers)

    $ python manage.py createsuperuser --username=joe --email=joe@example.com


### Alterando o password

É possível alterar a senha pelo terminal... 

    manage.py changepassword *username*

Ou via código...

    >>> from django.contrib.auth.models import User
    >>> u = User.objects.get(username='john')
    >>> u.set_password('new password')
    >>> u.save()


### Autenticando usuários

Para autenticar um *username* e um *password* utiliza a função `authenticate()`. Se autenticar, a função retorna o um
objeto `User`, se não, ela retorna `Null`.

```python
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
if user is not None:
    # the password verified for the user
    if user.is_active:
        print("User is valid, active and authenticated")
    else:
        print("The password is valid, but the account has been disabled!")
else:
    # the authentication system was unable to verify the username and password
    print("The username and password were incorrect.")
```



### Permissões e Autorizações

O sistema de permissões permite atribuir permissões a usuários específico e a grupos de usuários.

É o mesmo utilizado na app __admin__ do Django e seja bem vindo para utilizá-lo em seu próprio código.

Os métodos de manipulação são:

- has_add_permission(),
- has_change_permission() and
- has_delete_permission()

Tais métodos são fornecidos pela classe `ModelAdmin` e é possível customizar para diferentes objetos (object instances)
de mesmo tipo.

O objeto `User` possui dois campos de relacionamento muitos-para-muitos: `groups` e `user_permissions`
Os objetos `User` podem ser acessado pelos objetos relacionados na mesma direção de qualquer outro modelo (model) Django:

```python
myuser.groups = [group_list]
myuser.groups.add(group, group, ...)
myuser.groups.remove(group, group, ...)
myuser.groups.clear()
myuser.user_permissions = [permission_list]
myuser.user_permissions.add(permission, permission, ...)
myuser.user_permissions.remove(permission, permission, ...)
myuser.user_permissions.clear()
```


### Permissões Padrão

Quando a app `django.contrib.auth` é listada na seção INSTALLED_APPS isto garante que três permissões padrão são criadas
para cada model (model) Django definido em cada uma de suas aplicações:

- add,
- change and 
- delete

Elas são criadas quando executamos o comando `manage.py migrate`; na primeira vez que executamos o comando, as permissões
padrão serão criadas por todos os modelos previamente instalados, bem como para todos os modelos (models) que estão sendo
instalados naquele momento. Mais tarde, isto criará as permissões padrão para cada novo modelo toda vez que você
executar o comando.

Pressupondo que sua aplicação tenha como *app_label* `foo` e o modelo chama-se `Bar`, para testar as permissões você
poderia fazer:

    add: user.has_perm('foo.add_bar')
    change: user.has_perm('foo.change_bar')
    delete: user.has_perm('foo.delete_bar')


### Grupos

https://docs.djangoproject.com/en/dev/topics/auth/default/#groups


O modelo `django.contrib.auth.models.Group` é um caminho genérico de categorização de usuários no qual você pode aplicar
as permissões para aqueles usupários.

A user can belong to any number of groups.



### Criando permissões programaticamente

Enquanto as permissões customizadas podem ser definidas em um "model's Meta class", você também podera criar permissões
diretamente

Por exemplo, vocẽ poderá criar a permissão `can_publish` para o modelo `BlogPost` na `myapp`:

```python
from myapp.models import BlogPost
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(BlogPost)
permission = Permission.objects.create(codename='can_publish',
                                       name='Can Publish Posts',
                                       content_type=content_type)
```

A permissão pode ser atribuída ao `User` através do atributo `user_permissions` ou ao `Group` através do atributo `permissions`.


### Cache de permissão

https://docs.djangoproject.com/en/dev/topics/auth/default/#permission-caching



### Autenticação nas requisições web

https://docs.djangoproject.com/en/dev/topics/auth/default/#authentication-in-web-requests


### Como efetuar login

https://docs.djangoproject.com/en/dev/topics/auth/default/#how-to-log-a-user-out

```python
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
        else:
            # Return a 'disabled account' error message
            ...
    else:
        # Return an 'invalid login' error message.
        ...
```


### Como efetuar logout

https://docs.djangoproject.com/en/dev/topics/auth/default/#how-to-log-a-user-out


### Limitando acesso a usuários registrados

__The raw way:__¶

O caminho mais simples para limitar acesso as páginas é checando `request.user.is_authenticated()` e redirecionando
para a página de login:

```python
from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated():
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...
```
...ou mostre uma mensagem de erro:

```python
from django.shortcuts import render

def my_view(request):
    if not request.user.is_authenticated():
        return render(request, 'myapp/login_error.html')
    # ...
```


### Authentication Views

https://docs.djangoproject.com/en/dev/topics/auth/default/#module-django.contrib.auth.views


### Helper functions

https://docs.djangoproject.com/en/dev/topics/auth/default/#helper-functions


### Built-in forms

https://docs.djangoproject.com/en/dev/topics/auth/default/#module-django.contrib.auth.forms


### Managing users in the admin

https://docs.djangoproject.com/en/dev/topics/auth/default/#managing-users-in-the-admin