# Generated by Django 5.1.7 on 2025-06-09 18:19

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OrderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='👤 Имя')),
                ('phone', models.CharField(max_length=20, verbose_name='📞 Телефон')),
                ('address', models.TextField(blank=True, null=True, verbose_name='🏠 Адрес')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='✉️ Комментарий')),
                ('delivery', models.CharField(blank=True, max_length=255, null=True, verbose_name='🚚 Тип доставки')),
                ('delivery_price', models.PositiveIntegerField(default=0, verbose_name='🚚 Стоимость доставки')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='📅 Дата заказа')),
                ('status', models.CharField(choices=[('processing', '🆕 Новый'), ('completed', '✅ Подтвержден'), ('cancelled', '❌ Отменен')], default='processing', max_length=20, verbose_name='📋 Статус заказа')),
            ],
            options={
                'verbose_name': '🧾 Заказ',
                'verbose_name_plural': '🧾 Заказы',
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.PositiveIntegerField(verbose_name='🆔 ID товара')),
                ('product_name', models.CharField(max_length=255, verbose_name='📦 Название товара')),
                ('product_image', models.URLField(blank=True, null=True, verbose_name='🖼️ Картинка товара')),
                ('variant_id', models.PositiveIntegerField(verbose_name='🆔 ID варианта')),
                ('package_quantity', models.CharField(max_length=100, verbose_name='📦 Кол-во в упаковке')),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=10, verbose_name='💸 Цена за единицу')),
                ('quantity', models.PositiveIntegerField(default=1, verbose_name='🔢 Количество')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='order.ordermodel', verbose_name='🧾 Заказ')),
            ],
            options={
                'verbose_name': '📦 Товар заказа',
                'verbose_name_plural': '📦 Товары заказа',
            },
        ),
    ]
