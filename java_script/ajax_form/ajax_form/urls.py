from django.conf.urls import patterns, include, url
from django.contrib import admin
from ajax_form import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ajax_form.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^exemplo_01/', include('exemplo_01.urls')),
)
