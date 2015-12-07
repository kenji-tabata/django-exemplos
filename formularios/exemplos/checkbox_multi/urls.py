from django.conf.urls import patterns,  url
from checkbox_multi import views

urlpatterns = patterns('',

    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^ver-alternativas/(?P<pk>[0-9]+)/$', views.carregar, name='ver-alternativas'),
    url(r'^atualizar/(?P<pk>[0-9]+)/$', views.atualizar, name='atualizar'),
    url(r'^deletar/(?P<pk>[0-9]+)/$', views.deletar, name='deletar'),
)
