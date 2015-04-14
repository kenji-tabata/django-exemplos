from django.conf.urls import patterns, include, url
from django.contrib import admin
from try_except import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'try_except.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^add_session/$', views.add_session, name='add_session'),
    url(r'^del_session/$', views.del_session, name='del_session')
)
