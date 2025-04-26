from rest_framework import viewsets

from dynamic.models import CarouselItem
from dynamic.serializer import CarouselItemSerializer

class CarouselViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarouselItem.objects.filter(allowed=True)
    serializer_class = CarouselItemSerializer
    pagination_class = None 