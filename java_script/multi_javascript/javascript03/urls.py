from django.conf.urls import url

from javascript03 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]