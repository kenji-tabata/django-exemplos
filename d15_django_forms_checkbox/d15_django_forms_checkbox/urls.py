from django.conf.urls import patterns, include, url
from django.contrib import admin
from d15_django_forms_checkbox import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd15_django_forms_checkbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^enviar/$', views.enviar, name="enviar")
)
