from django.urls import path
from .views import *


urlpatterns = [
    path('home/products', ProductListAPIView.as_view(), name="product-list"),
    path('categories/', CategoryListAPIView.as_view(), name="categories"),
    path('sub-categories/', SubCategoryListAPIView.as_view(), name="sub-categories"),
    path('product-detail/<int:pk>/', ProductDetailAPIView.as_view(), name="product-detail"),
    path('create-order/<int:pk>/', CreateOrderAPIView.as_view(), name="create-order"),
    path('review/<int:pk>/', ReviewAPIView.as_view(), name="review"),
    path('contacts/', ContactAPIView.as_view(), name="contacts"),
    path('questions/', QuestionAPIView.as_view(), name="questions")
]