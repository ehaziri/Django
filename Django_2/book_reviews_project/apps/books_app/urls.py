from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^create$', views.create, name='create'),
    url(r'^show_book/(?P<id>\d+)$', views.show_book, name='show_book'),
    url(r'^show_creator/(?P<id>\d+)$', views.show_creator, name='show_creator'),
    url(r'^add_review/(?P<id>\d+)$', views.add_review, name='add_review'),
    url(r'^delete_review/(?P<id>\d+)$', views.delete_review, name='delete_review'),
]
