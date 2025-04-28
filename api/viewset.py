from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

from django_filters.rest_framework import DjangoFilterBackend

from api.filters import ProductFilter, ProductPagination

from api.serializer import (
    BrandSerializer, 
    ProductListSerializer, 
    ProductDetailSerializer, 
    CategorySerializer
)

from product.models import (
    ProductVariantsModel,
    ProductImageModel, 
    CategoryModel, 
    ProductModel, 
    BrandModel, 
)

# Category viewset
class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CategoryModel.objects.filter(allowed=True)
    serializer_class = CategorySerializer
    pagination_class = None 
    
# Brand viewset
class BrandViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = BrandModel.objects.filter(allowed=True)
    serializer_class = BrandSerializer
    pagination_class = None 

# Product viewset
class ProductViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ProductModel.objects.filter(allowed=True).prefetch_related(
        Prefetch('variants', queryset=ProductVariantsModel.objects.filter(allowed=True)),
        Prefetch('images', queryset=ProductImageModel.objects.filter(allowed=True)),
        'category',
        'brand',
    )
    def get_serializer_class(self):
        if self.action == 'list':
            return ProductListSerializer
        return ProductDetailSerializer

    filterset_class = ProductFilter
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ['name', 'description', 'brand__name', 'detail', 'category__name']
    ordering_fields = ['price', 'name']  # Sort qilish: ?ordering=price yoki ?ordering=-price (kamayish tartibida)
    pagination_class = None


    