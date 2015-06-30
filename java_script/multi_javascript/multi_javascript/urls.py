from django.conf.urls import patterns, include, url
from django.contrib import admin
from multi_javascript import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'multi_javascript.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^javascript01/', include('javascript01.urls', namespace='javascript01')),
    url(r'^javascript02/', include('javascript02.urls', namespace='javascript02')),
    url(r'^javascript03/', include('javascript03.urls', namespace='javascript03')),
    url(r'^$', views.index, name='index'),
    url(r'^pagina/$', views.pagina, name='pagina'),
)
