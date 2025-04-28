from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.viewset import CategoryViewSet, BrandViewSet, ProductViewSet
from dynamic.viewset import CarouselViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'carousels', CarouselViewSet)

urlpatterns = [
    path('', include(router.urls)),
]