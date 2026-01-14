from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = 'order'

urlpatterns = [
    path("checkout/", views.OrderCheckoutView.as_view(), name="checkout" ),
]