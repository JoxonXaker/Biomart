from django.db import models
from django.utils import timezone

ORDER_STATUS_CHOICES = (
    ('new', '🆕 Новый'),
    ('confirmed', '✅ Подтвержден'),
    ('cancelled', '❌ Отменен'),
)

class CheckOrderModel(models.Model):
    data = models.JSONField(verbose_name="📦 Данные заказа")
    status = models.CharField(
        max_length=10,
        choices=ORDER_STATUS_CHOICES,
        default='new',
        verbose_name="📌 Статус"
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="🕒 Дата создания")

    class Meta:
        verbose_name = "📄 Чек"
        verbose_name_plural = "📄 Все чеки"

    def __str__(self):
        return f"Чек - {self.get_status_display()} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
