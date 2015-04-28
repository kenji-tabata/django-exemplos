from django.conf.urls import url
from exemplo_01 import views

urlpatterns = [
    url(r'^$', views.index, name='index_exemplo_01'),
    url(r'^filtrar_cidade/$', views.filtrar_cidade, name='filtrar_cidade'),
]