from django.conf.urls import patterns, include, url
from django.contrib import admin
from d03_template import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd03_template.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.base, name='base'),
    url(r'^index$', views.index, name='index'),
    url(r'^pagina$', views.pagina, name='pagina'),
)
