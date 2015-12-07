from django.conf.urls import patterns, url
from textbox_forms import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)
