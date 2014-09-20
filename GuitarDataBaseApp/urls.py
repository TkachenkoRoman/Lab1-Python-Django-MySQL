from django.conf.urls import url

from GuitarDataBaseApp import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^#GuitarTypes/', views.guitar_types_view, name='guitar_types'),
    url(r'^#Pickups/', views.pickups_view, name='pickups'),
)