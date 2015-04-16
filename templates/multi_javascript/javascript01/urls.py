from django.conf.urls import url

from javascript01 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]