from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^wish_items/create/$', views.create, name="create"),
    url(r'^add/$', views.add, name="add"),
    url(r'^add_wish/(?P<id>\d+)$', views.add_wish, name="add_wish"),
    url(r'^show_item/(?P<id>\d+)$', views.show_item, name="show_item"),
    url(r'^remove_wish/(?P<id>\d+)$', views.remove_wish, name="remove_wish"),
    url(r'^delete/(?P<id>\d+)$', views.delete, name="delete"),
]
