from django.contrib import admin
from django.urls import path, include
from app_episound import views

urlpatterns = [
    path('', views.index, name="index"),
]
