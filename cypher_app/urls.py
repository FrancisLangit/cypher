"""Defines URL patterns for cypher_app."""

from django.urls import path

from . import views

app_name = 'cypher_app'
urlpatterns = [
	# Home page
	path('', views.index, name='index')
]