from django.conf.urls import patterns, include, url
from django.contrib import admin
from d12_view_html_code import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd12_view_html_code.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index')
)
