from django.conf.urls import patterns, include, url
from django.contrib import admin
from d09_login import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd09_login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'django.contrib.auth.views.login', {'template_name': 'd09_login/login.html','redirect_field_name': ''}),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^logado/$', views.logado, {}),
)
