from django.apps import AppConfig


class DynamicConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'dynamic'

    verbose_name = "Управление сайтом"

