"""Defines URL patterns for cypher_app."""

from django.urls import path

from . import views

app_name = 'cypher_app'
urlpatterns = [
	# Home
	path('', views.index, name='index'),

	# Cipher Pages
	path('caesar_cipher', views.caesar_cipher, name='caesar_cipher')
]