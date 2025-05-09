# Generated by Django 5.1.7 on 2025-04-22 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_brandmodel_country_brandmodel_website_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='allowed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
