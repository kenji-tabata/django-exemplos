from django.conf.urls import patterns, include, url
from django.contrib import admin
from raw_query import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'raw_query.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^select_all/$', views.select_all, name='mostrar_todos'),
    url(r'^select_id/(?P<pk>[0-9]+)$', views.select_id, name='mostrar_pelo_id'),
    url(r'^select_translation/$', views.select_translation, name='mostrar_translation'),
    url(r'^select_first/$', views.select_first, name='mostrar_primeiro'),
    url(r'^select_filter/$', views.select_filter, name='mostrar_filtro'),
    url(r'^select_order_desc/$', views.select_order_desc, name='mostrar_ordem_desc'),
    url(r'^select_like/(?P<nome>\w+)/$', views.select_like, name='mostrar_like'),
    url(r'^select_inner_join/$', views.select_inner_join, name='mostrar_todos_inner_join'),
)
