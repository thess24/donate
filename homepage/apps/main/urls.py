from django.conf.urls import patterns, url
from apps.main import views

 

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^list/', views.list, name='list'),
    url(r'^managewidgets/', views.managewidgets, name='managewidgets'),
)