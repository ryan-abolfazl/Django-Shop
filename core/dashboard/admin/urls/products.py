from django.urls import path, include, re_path
from .. import views

urlpatterns = [
    path('product/list/', views.AdminProductListView.as_view(), name='product-list'),
    # re_path(r'product/(?P<slug>[-\w]+)/detail', views.ShopProductDetailView.as_view(), name='product-detail'),
    ]