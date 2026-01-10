from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = "dashboard"

urlpatterns = [
    path("home/", views.DashboardHomeView.as_view(), name="home" ),

    #include admin urls
    path("admin/", include('dashboard.admin.urls')),

    #include customer urls
    path("customer/", include('dashboard.customer.urls')),
]