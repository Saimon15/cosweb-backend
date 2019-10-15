from django.urls import path
from .views import ProductCategoryView, ProductView, ProductDetailView

urlpatterns = [
    path('', ProductView.as_view()),
    path('<int:pk>', ProductDetailView.as_view()),
    path('categories/', ProductCategoryView.as_view()),
]
