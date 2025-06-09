from rest_framework import serializers
from .models import OrderModel, OrderItemModel


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItemModel
        fields = [
            "product_id",
            "product_name",
            "product_image",
            "variant_id",
            "package_quantity",
            "price",
            "quantity",
            "total_price"
        ]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_items_price = serializers.SerializerMethodField()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = OrderModel
        fields = [
            "id",
            "name",
            "phone",
            "address",
            "comment",
            "delivery",
            "delivery_price",
            "date",
            "status",
            "items",
            "total_items_price",
            "total_price"
        ]

    def get_total_items_price(self, obj):
        return obj.total_items_price()

    def get_total_price(self, obj):
        return obj.total_price()
