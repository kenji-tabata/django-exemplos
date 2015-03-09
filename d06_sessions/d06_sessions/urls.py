from django.conf.urls import patterns, include, url
from django.contrib import admin
from d06_sessions import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd06_sessions.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^getNome$', views.getNome, name='getNome'),
)
