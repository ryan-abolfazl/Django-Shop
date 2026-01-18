from .. import views
from django.shortcuts import redirect
from django.urls import path, include

urlpatterns = [
    path("wishlist/list/", views.CustomerWishlistListView.as_view(), name="wishlist-list"),
]