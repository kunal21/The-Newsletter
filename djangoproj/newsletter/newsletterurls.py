from django.conf.urls import url
from django.contrib import admin
from newsletter import views
from . import forms

urlpatterns = [
	url(r'^homepage/$',views.newsletter_home_page,name="homepage"),
	url(r'^espn/$',views.newsletter_espn,name="espn"),
	url(r'^about/$',views.newsletter_about,name="about"),
	url(r'^technology/$',views.newsletter_technology,name="technology"),
	

]