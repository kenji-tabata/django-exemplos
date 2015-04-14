from django.conf.urls import patterns, include, url
from django.contrib import admin
from testando_model import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testando_model.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
)
