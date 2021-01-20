"""Defines URL patterns for cypher project."""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cypher_app.urls')),
]
