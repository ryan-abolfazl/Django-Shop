from . import views
from django.shortcuts import redirect
from django.urls import path, include

app_name = 'payment'

urlpatterns = [
    path("verify", views.PaymentVerifyView.as_view(), name="verify" ),
]