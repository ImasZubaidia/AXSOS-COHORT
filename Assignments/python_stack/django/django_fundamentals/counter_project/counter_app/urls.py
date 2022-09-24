from django.contrib import admin
from django.urls import path 
from .import views

urlpatterns = [
    path('', views.refresh_counter),
    path('destroy_session', views.destroy)
]
