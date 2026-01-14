from .. import views
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("address/list/", views.CustomerAddressListView.as_view(), name="address-list"),
    path("address/create/", views.CustomerAddressCreateView.as_view(), name="address-create"),
    path("address/<int:pk>/edit/", views.CustomerAddressUpdateView.as_view(), name="address-edit"),
    path("address/<int:pk>/delete/", views.CustomerAddressDeleteView.as_view(), name="address-delete"),
    ]