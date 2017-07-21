from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^ninjas/(?P<color>[a-zA-Z0-9]*)$', views.ninja, name="ninja")
]
