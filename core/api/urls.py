from django.urls import path, include
from .views import CategoryListView, ProductListView, ProductDetailView, ProjectViewSet,ProjectDetailView
from rest_framework.routers import DefaultRouter

# Initialize the router and register viewsets
router = DefaultRouter()
router.register(r'projects', ProjectViewSet, basename='projects')


# Define urlpatterns by including both the manually defined paths and router URLs
urlpatterns = [
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('', include(router.urls)),  # Include router-generated URLs
]
