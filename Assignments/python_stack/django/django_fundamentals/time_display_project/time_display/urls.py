from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('time_display', views.index)
]
