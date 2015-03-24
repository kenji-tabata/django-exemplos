from django.conf.urls import patterns, include, url
from django.contrib import admin
from d13_combobox_array import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd13_combobox_array.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
)
