from django.conf.urls import patterns, include, url
from django.contrib import admin
from login_session import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login_session.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^logado/$', views.logado, {}),
)
