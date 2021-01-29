"""Defines URL patterns for cypher_app."""

from django.urls import path

from . import views


app_name = 'cypher_app'
urlpatterns = [
	# Home
	path('', views.index, name='index'),

	# App Page
	path('app/<str:cipher_choice>/', views.app, name='app'),
	path('app/<str:cipher_choice>/output', views.app_output, 
		name='app_output'),

	# About Page
	path('about/', views.about, name='about')
]