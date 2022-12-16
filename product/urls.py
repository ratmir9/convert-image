from django.urls import path
from product.views import ProductListAPIView, ProductDetailAPIView

urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductListAPIView.as_view())
]