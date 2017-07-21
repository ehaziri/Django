from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^dashboard/(?P<level>[a-zA-Z0-9]*)$', views.dashboard, name='dashboard'),
    url(r'^board/$', views.board, name='board'),
    url(r'^add/$', views.add, name='add'),
    url(r'^users/new$', views.new, name='new'),
    url(r'^users/edit/(?P<id>\d+)$', views.edit, name='edit'),
    url(r'^users/profile$', views.profile, name='profile'),
    url(r'^update/(?P<id>\d+)$', views.update, name='update'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^delete/(?P<id>\d+)$', views.destroy, name='destroy'),
    url(r'^show/(?P<id>\d+)$', views.show, name='show'),
    url(r'^addmessage/(?P<id>\d+)$', views.addmessage, name='addmessage'),
    url(r'^addcomment/(?P<id>\d+)$', views.addcomment, name='addcomment')
]
