from django.conf.urls import patterns, url
from dj_02_criando_links import views

urlpatterns = patterns('',
    url(r'^dj-02$', views.index, name='index'),
    url(r'^dj-02/pagina01$', views.pagina01, name='pagina01'),
    url(r'^dj-02/pagina02$', views.pagina02, name='pagina02'),
)