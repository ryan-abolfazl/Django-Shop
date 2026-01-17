from .. import views
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("order/list/", views.CustomerOrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/detail/", views.CustomerOrderDetailView.as_view(), name="order-detail"),
]