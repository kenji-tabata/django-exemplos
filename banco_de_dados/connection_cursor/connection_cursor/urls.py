from django.conf.urls import patterns, include, url
from django.contrib import admin
from connection_cursor import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'connection_cursor.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^select_all/$', views.select_all, name='select_all'),
    url(r'^select_id/(?P<pk>[0-9]+)/$', views.select_id, name='mostrar_pelo_id'),
    url(r'^select_first/$', views.select_first, name='mostrar_primeiro'),
    url(r'^select_filter/$', views.select_filter, name='mostrar_filtro'),
    url(r'^select_order_desc/$', views.select_order_desc, name='mostrar_ordem_desc'),
    url(r'^select_like/(?P<nome>\w+)/$', views.select_like, name='mostrar_like'),
    url(r'^select_inner_join/$', views.select_inner_join, name='mostrar_todos_inner_join'),
    url(r'^select_combined/$', views.select_combined, name='mostrar_especifico'),
    url(r'^insert_usuario/$', views.insert_usuario, name='ins_usuario'),
    url(r'^insert_comentario/$', views.insert_comentario, name='ins_cometario'),
    url(r'^update_usuario/(?P<pk>[0-9]+)/$', views.update_usuario, name='up_usuario'),
    url(r'^delete_usuario/(?P<pk>[0-9]+)/$', views.delete_usuario, name='del_usuario'),
)
