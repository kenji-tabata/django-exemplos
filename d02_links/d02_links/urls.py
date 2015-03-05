from django.conf.urls import patterns, include, url
from django.contrib import admin
from d02_links import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd02_links.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^pagina01$', views.pagina01, name='pagina01'),
    url(r'^pagina02$', views.pagina02, name='pagina02'),
    
)
