from django.conf.urls import patterns, url

from app02 import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
)
