from django.conf.urls import patterns, include, url
from django.contrib import admin
from d14_django_forms_textbox import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'd14_django_forms_textbox.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name="index"),
    url(r'^enviar/$', views.enviar, name="enviar")
)
