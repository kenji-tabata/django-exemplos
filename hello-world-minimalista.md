Hello World Minimalista
===

Eis a menor aplicação Django possível...

```python
#
# Settings
#
from django.conf import settings

settings.configure(
    DEBUG = True,
    ALLOWED_HOSTS = ['localhost'],
    ROOT_URLCONF = '__main__',
    MIDDLEWARE_CLASSES = (
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

#
# View
#
from django.conf.urls import url
from django.http import HttpResponse

def index(request):
    return HttpResponse('Hello World')

urlpatterns = (
    url(r'^$', index),
)


#
# Terminal
#
import sys
from django.core.management import execute_from_command_line
execute_from_command_line(sys.argv)
```
