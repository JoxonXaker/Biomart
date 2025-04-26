from rest_framework import serializers
from dynamic.models import CarouselItem

class CarouselItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarouselItem
        fields = ['id', 'title', 'image', 'description', 'link']
