from rest_framework.routers import DefaultRouter
from django.urls import path, include

from dynamic.viewset import CarouselViewSet

router = DefaultRouter()
router.register(r'carousel', CarouselViewSet)

urlpatterns = [
    path('dynamic/', include(router.urls)),
]