from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils.dateparse import parse_datetime
from decimal import Decimal
from order.models import OrderModel, OrderItemModel
from order.serializers import OrderSerializer
from order.tasks import send_order_telegram_message


class OrderViewSet(viewsets.ViewSet):
    """
    Buyurtmalarni ko‘rish va yaratish uchun ViewSet.
    """

    def list(self, request):
        orders = OrderModel.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        orders_data = request.data

        for order_data in orders_data:
            delivery_type = order_data.get("delivery", "")
            items = order_data.get("items", [])
            
            # Umumiy narxni hisoblash
            total_price = Decimal(0)
            for item in items:
                variant = item.get("variant", {})
                quantity = Decimal(item.get("quantity", 1))
                price = Decimal(variant.get("price", 0))
                total_price += price * quantity

            # Yetkazib berish narxini aniqlash
            if delivery_type.strip() == "Доставка по всем регионам":
                if total_price >= 1_000_000:
                    delivery_price = 0
                else:
                    delivery_price = 50000
            else:
                delivery_price = int(order_data.get("delivery_price", 0))

            # Orderni yaratish
            order = OrderModel.objects.create(
                name=order_data.get("name"),
                phone=order_data.get("phone"),
                address=order_data.get("address", ""),
                comment=order_data.get("comment", ""),
                delivery=delivery_type,
                delivery_price=delivery_price,
                date=parse_datetime(order_data.get("date")),
            )

            # OrderItem yaratish
            for item in items:
                product = item.get("product", {})
                variant = item.get("variant", {})

                OrderItemModel.objects.create(
                    order=order,
                    product_id=product.get("id"),
                    product_name=product.get("name"),
                    product_image=product.get("image", ""),
                    variant_id=variant.get("id"),
                    package_quantity=variant.get("package_quantity", ""),
                    price=Decimal(variant.get("price", 0)),
                    quantity=item.get("quantity", 1),
                )

        
        send_order_telegram_message(order)

        return Response({"detail": "Buyurtmalar yaratildi ✅"}, status=status.HTTP_201_CREATED)

   
    def update(self, request, pk=None):
        return Response({"detail": "Tahrirlash taqiqlangan ❌"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, pk=None):
        return Response({"detail": "Tahrirlash taqiqlangan ❌"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk=None):
        return Response({"detail": "O'chirish taqiqlangan ❌"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
