Criando usuários
===

[https://docs.djangoproject.com/en/1.8/topics/auth/default/#creating-users](https://docs.djangoproject.com/en/1.8/topics/auth/default/#creating-users)

Pelo terminal interativo do Python...

```python
from django.contrib.auth.models import User
user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
user.last_name = 'Lennon'
user.save()
```

Pelo terminal do Linux...

    python manage.py createsuperuser