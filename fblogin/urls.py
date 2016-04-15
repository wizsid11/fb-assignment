from django.conf.urls import url, include
from django.contrib import admin
from .views import (login,home,logout,new)

urlpatterns = [
    url(r'^$', login),
    url(r'^home/$', home),
    url(r'^logout/$', logout),
    url(r'^detail/$', new)
]
