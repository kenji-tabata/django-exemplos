from django.conf.urls import patterns, include, url
from django.contrib import admin
from testando_view import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testando_view.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^adicionar/$', views.adicionar, name='adicionar'),
    url(r'^enviar/$', views.enviar, name='enviar'),
    url(r'^editar/(?P<pk>[0-9]+)/$', views.editar, name='editar'),
    url(r'^deletar/(?P<pk>[0-9]+)/$', views.deletar, name='deletar'),
    url(r'^detalhes/(?P<pk>[0-9]+)/$', views.detalhes, name='detalhes'),
)
