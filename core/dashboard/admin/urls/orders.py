from .. import views
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("order/list/", views.AdminOrderListView.as_view(), name="order-list"),
    path("orders/<int:pk>/detail/", views.AdminOrderDetailView.as_view(), name="order-detail"),
    path("orders/<int:pk>/invoice/", views.AdminOrderInvoiceView.as_view(), name="order-invoice"),
]