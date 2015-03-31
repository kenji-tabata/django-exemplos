from django.conf.urls import patterns, include, url
from django.contrib import admin
from u01_combobox_lista_estados import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'u01_combobox_lista_estados.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar')
)
