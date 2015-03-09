from django.conf.urls import patterns, include, url
from django.contrib import admin
from d04_metodo_get import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd04_metodo_get.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
)
