from django.conf.urls import patterns, include, url
from django.contrib import admin
from local_flavor_form_validacao import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'local_flavor_form_validacao.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar')
)
