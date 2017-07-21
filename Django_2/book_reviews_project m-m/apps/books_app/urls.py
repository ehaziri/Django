from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^create$', views.create, name='create'),
    # url(r'^register$', views.register, name='register'),
    # url(r'^success$', views.success, name='success'),
    # url(r'^logout$', views.logout, name='logout'),
]
