from django.conf.urls import url

from GuitarDataBaseApp import views

urlpatterns = (
    url(r'^$', views.index, name='index'),
    url(r'^GuitarTypes/', views.guitar_types_view, name='guitar_types'),
    url(r'^Pickups/', views.pickups_view, name='pickups'),
    url(r'^Produser/', views.produsers_view, name='produsers'),
    url(r'^Bridge/', views.bridge_view, name='bridges'),
    url(r'^Body/', views.body_view, name='bodies'),
    url(r'^Guitar/', views.guitar_view, name='guitars'),
    url(r'^(?P<edit_id>\d+)/Edit/', views.edit_view, name='edit'),
    url(r'^Add/', views.add_view, name='add'),
    url(r'^(?P<delete_id>\d+)/Delete/', views.delete_view, name='delete'),
    url(r'^Edit/confirm/', views.edit_confirm_view, name='edit_confirm'),
    url(r'^Add_confirm/', views.add_confirm_view, name='add_confirm'),
    url(r'^load_csv/', views.load_csv_view, name='load_csv'),
    url(r'^Guitar_filter/', views.filter_view, name='filter'),
    url(r'^Guitar_filter_check/', views.filter_check, name='filter_check'),
    url(r'^Search/', views.search_view, name='search'),
)