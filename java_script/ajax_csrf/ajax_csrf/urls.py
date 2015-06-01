from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax_csrf import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajax_csrf.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
    url(r'^enviar_comentario', views.enviar_comentario, name='enviar_comentario')
)
