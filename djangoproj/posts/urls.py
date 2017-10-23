from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^create/$',views.create),
	url(r'^list/$',views.list),
	url(r'^(?P<id>\d+)/$',views.detail,name="detail"),
	url(r'^(?P<id>\d+)/edit/$',views.update),
	url(r'^(?P<id>\d+)/delete/$',views.delete),
	]