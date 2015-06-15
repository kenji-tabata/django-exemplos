from django.conf.urls import patterns, include, url
from django.contrib import admin
from login_class import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login_class.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^home/$', views.home, name='home'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name='logout'),
)
