from rest_framework.routers import DefaultRouter
from django.urls import path, include

from api.viewset import CategoryViewSet, BrandViewSet, ProductViewSet, VariantsViewSet
from dynamic.viewset import CarouselViewSet
from order.views import OrderViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'brands', BrandViewSet)
router.register(r'products', ProductViewSet)
router.register(r'variants', VariantsViewSet)
router.register(r'carousels', CarouselViewSet)
router.register(r'orders', OrderViewSet, basename='orders')


urlpatterns = [
    path('', include(router.urls)),
]