from .. import views
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("home/", views.CustomerDashboardHomeView.as_view(), name="home" ),
    ]