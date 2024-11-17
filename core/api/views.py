from rest_framework import generics
from .models import Category, Product ,ProductImage, Projects
from .serializers import CategorySerializer, ProductSerializer , ProjectsSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Prefetch
from django.core.cache import cache
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django_filters import rest_framework as filters

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.filter(parent__isnull=True)  # Only top-level categories
    serializer_class = CategorySerializer


class ProductFilter(filters.FilterSet):
    search = filters.CharFilter(method='filter_by_name')

    class Meta:
        model = Product
        fields = ['category', 'search']

    def filter_by_name(self, queryset, name, value):
        return queryset.filter(name_AR__icontains=value) | queryset.filter(name_EN__icontains=value)

class ProductListView(generics.ListAPIView):
    queryset = Product.objects.prefetch_related(
        Prefetch('images', queryset=ProductImage.objects.only('image'))
    ).select_related('category')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProductFilter

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CachedCategoryListView(APIView):
    def get(self, request, *args, **kwargs):
        categories = cache.get('categories')
        if not categories:
            categories = CategorySerializer(Category.objects.filter(parent__isnull=True), many=True).data
            cache.set('categories', categories, timeout=60 * 60)  # Cache for 1 hour
        return Response(categories)
    

class ProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer 