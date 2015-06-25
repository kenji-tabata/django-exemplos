from django.conf.urls import patterns, include, url
from django.contrib import admin
from lista_filtro import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'lista_filtro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^ordem_asc/(?P<tipo>\w+)/$', views.order_by_asc, name='ordem_asc'),
    url(r'^ordem_desc/(?P<tipo>\w+)/$', views.order_by_desc, name='ordem_desc'),
    url(r'^ordem_ult/(?P<tipo>\w+)/$', views.order_by_ult, name='ordem_ult'),
)
