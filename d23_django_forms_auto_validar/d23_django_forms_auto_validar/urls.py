from django.conf.urls import patterns, include, url
from django.contrib import admin
from d23_django_forms_auto_validar import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd23_django_forms_auto_validar.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^listar$', views.listar, name='listar')
)
