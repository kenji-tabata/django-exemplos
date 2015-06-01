from django.conf.urls import patterns, include, url
from django.contrib import admin
from multi_database_intro import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'multi_database_intro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^trocar/(?P<tipo>\w+)/$', views.trocar, name='trocar'),
)
