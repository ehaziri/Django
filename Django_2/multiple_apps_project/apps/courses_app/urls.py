from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^create$', views.create, name="create"),
    url(r'^remove/(?P<id>\d+)$', views.remove, name="remove"),
    url(r'^destroy/(?P<id>\d+)$', views.destroy, name="destroy"),
    url(r'^add/(?P<id>\d+)$', views.add, name="add"),
    url(r'^show/(?P<id>\d+)$', views.show, name="show"),
    url(r'^remove_comment/(?P<id>\d+)$', views.remove_comment, name="remove_comment"),
]
