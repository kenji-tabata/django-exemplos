from django.conf.urls import patterns, include, url
from django.contrib import admin
from d00_base_projeto import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd00_base_projeto.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
)
