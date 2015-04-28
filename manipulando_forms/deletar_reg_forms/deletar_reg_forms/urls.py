from django.conf.urls import patterns, include, url
from django.contrib import admin
from deletar_reg_forms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'deletar_reg_forms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^listar/$', views.listar, name='listar'),
    url(r'^deletar/(?P<pk>[0-9]+)/$', views.deletar, name='deletar')
)
