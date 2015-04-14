from django.conf.urls import patterns, include, url
from django.contrib import admin
from template_html import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'template_html.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^base$', views.base, name='base'),
    url(r'^$', views.index, name='index'),
    url(r'^pagina$', views.pagina, name='pagina'),
)
