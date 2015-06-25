from django.conf.urls import url

from javascript02 import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]