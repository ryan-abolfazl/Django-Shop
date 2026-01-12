from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = "admin"

urlpatterns = [
    path("home/", views.AdminDashboardHomeView.as_view(), name="home" ),
    path("security-edit/", views.AdminSecurityEditView.as_view(), name="security-edit" ),
    path("profile-edit/", views.AdminProfileEditView.as_view(), name="profile-edit" ),
    ]