from django.conf.urls import patterns, include, url
from django.contrib import admin
from d05_metodo_post import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd05_metodo_post.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^result$', views.result, name='result'),
)
