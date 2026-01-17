from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = 'order'

urlpatterns = [
    path("checkout/", views.OrderCheckoutView.as_view(), name="checkout" ),
    path("completed/",views.OrderCompletedView.as_view(),name="completed"),
    path("failed/",views.OrderFailedView.as_view(),name="failed"),
    path("validate-coupon/",views.ValidateCouponView.as_view(),name="validate-coupon"),
]