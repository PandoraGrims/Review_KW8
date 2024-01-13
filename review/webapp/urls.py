from django.urls import path

from webapp.reviews import CreateReviewView, UpdateReviewView, DeleteReviewView
from webapp.views import ProductListView, ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView

app_name = "webapp"

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('product/<int:pk>', ProductDetailView.as_view(), name="product_detail_view"),
    path('product/add/', ProductCreateView.as_view(), name="product_create"),
    path('product/<int:pk>/update', ProductUpdateView.as_view(), name="product_update_view"),
    path('product/<int:pk>/delete', ProductDeleteView.as_view(), name="product_delete_view"),

    path('product/<int:pk>/reviews/create/', CreateReviewView.as_view(), name='create_review'),
    path('product/<int:product_id>/reviews/<int:pk>/edit/', UpdateReviewView.as_view(), name='edit_review'),
    path('product/<int:product_id>/reviews/<int:pk>/delete/', DeleteReviewView.as_view(), name='delete_review'),

]
