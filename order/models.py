from django.db import models
from django.utils import timezone
from django.utils.safestring import mark_safe



class OrderModel(models.Model):
    STATUS_CHOICES = [
        ('processing', "🆕 Новый"),
        ('completed', "✅ Подтвержден"),
        ('cancelled', "❌ Отменен"),
    ]

    name = models.CharField(max_length=100, verbose_name="👤 Имя")
    phone = models.CharField(max_length=20, verbose_name="📞 Телефон")
    address = models.TextField(blank=True, null=True, verbose_name="🏠 Адрес")
    comment = models.TextField(blank=True, null=True, verbose_name="✉️ Комментарий")

    delivery = models.CharField(max_length=255, blank=True, null=True, verbose_name="🚚 Тип доставки")
    delivery_price = models.PositiveIntegerField(default=0, verbose_name="🚚 Стоимость доставки")


    date = models.DateTimeField(default=timezone.now, verbose_name="📅 Дата заказа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='processing', verbose_name="📋 Статус заказа")

    class Meta:
        verbose_name = "🧾 Заказ"
        verbose_name_plural = "🧾 Заказы"
        ordering = ['-date']

    def __str__(self):
        return f"{self.name} — {self.phone} ({self.get_status_display()})"

    def total_items_price(self):
        return sum(item.total_price() for item in self.items.all())

    def total_price(self):
        return self.total_items_price() + self.delivery_price


class OrderItemModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE, related_name="items", verbose_name="🧾 Заказ")

    product_id = models.PositiveIntegerField(verbose_name="🆔 ID товара")
    product_name = models.CharField(max_length=255, verbose_name="📦 Название товара")
    product_image = models.URLField(blank=True, null=True, verbose_name="🖼️ Картинка товара")

    variant_id = models.PositiveIntegerField(verbose_name="🆔 ID варианта")
    package_quantity = models.CharField(max_length=100, verbose_name="📦 Кол-во в упаковке")
    price = models.DecimalField(max_digits=10, decimal_places=0, default=0, verbose_name="💸 Цена за единицу")
    quantity = models.PositiveIntegerField(default=1, verbose_name="🔢 Количество")

    class Meta:
        verbose_name = "📦 Товар заказа"
        verbose_name_plural = "📦 Товары заказа"

    def __str__(self):
        return f"{self.product_name} × {self.quantity}"

    def total_price(self):
        return self.price * self.quantity
    
    def display_image(self):
        if self.product_image:
            return mark_safe(f'<a href="{self.product_image}" data-lightbox="image"><img src="{self.product_image}" width="45" height="45" style="border: 1px solid #e8e8e8;"/></a>')
        return mark_safe(f'<img src="/media/admin-interface/helper/image.png" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')


    

