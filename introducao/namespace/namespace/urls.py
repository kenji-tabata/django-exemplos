from django.conf.urls import patterns, include, url
from django.contrib import admin
from namespace import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^app01/$', include('app01.urls', namespace='app01', app_name='app01')),
    url(r'^app02/$', include('app02.urls', namespace='app02', app_name='app02')),
    url(r'^$', views.index, name='index'),
)
