from django.urls import path, include, re_path
from .. import views

urlpatterns = [
    path('reviews/list/', views.AdminReviewListView.as_view(), name='review-list'),
    path('reviews/<int:pk>/edit/', views.AdminReviewsUpdateView.as_view(), name='review-edit'),
]