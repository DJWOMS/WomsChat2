# coding=utf-8
from django.urls import path
from start import views

urlpatterns = [
    path('', views.start),
]