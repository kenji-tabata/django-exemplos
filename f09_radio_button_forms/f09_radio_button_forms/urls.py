from django.conf.urls import patterns, include, url
from django.contrib import admin
from f09_radio_button_forms import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'f09_radio_button_forms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name='enviar'),
)
