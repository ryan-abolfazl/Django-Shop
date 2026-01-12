from django.urls import path, include, re_path
from .. import views

urlpatterns = [
    path('product/list/', views.AdminProductListView.as_view(), name='product-list'),
    path('product/<int:pk>/edit', views.AdminProductUpdateView.as_view(), name='product-edit'),
    ]