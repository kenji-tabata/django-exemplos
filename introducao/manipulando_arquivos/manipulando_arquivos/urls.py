from django.conf.urls import patterns, include, url
from django.contrib import admin
from manipulando_arquivos import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'manipulando_arquivos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^criar_arquivo/$', views.criar_arquivo, name='criar_arquivo'),
    url(r'^(?P<tipo>\w+)/$', views.ler_arquivo, name='ler_arquivo'),
    url(r'^salvar_arquivo/(?P<tipo>\w+)/$', views.salvar_arquivo, name='salvar_arquivo'),
    url(r'^deletar_arquivo/$', views.deletar_arquivo, name='deletar_arquivo')
)
