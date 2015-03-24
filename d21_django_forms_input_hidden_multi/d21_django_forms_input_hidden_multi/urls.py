from django.conf.urls import patterns, include, url
from django.contrib import admin
from d21_django_forms_input_hidden_multi import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd21_django_forms_input_hidden_multi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^enviar/$', views.enviar, name="enviar")
)
