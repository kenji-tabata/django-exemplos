from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exemplos.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^checkbox/', include('checkbox.urls', namespace='checkbox')),
    url(r'^checkbox_multi/', include('checkbox_multi.urls', namespace='checkbox_multi')),
    url(r'^textbox/', include('textbox.urls', namespace='textbox')),
    url(r'^textbox_forms/', include('textbox_forms.urls', namespace='textbox_forms')),
)
