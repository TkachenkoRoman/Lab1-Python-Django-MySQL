from django.conf.urls import url

from GuitarDataBaseApp import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
)