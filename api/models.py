from django.db import models
from admin_interface.models import Theme
from django.utils.translation import gettext_lazy as _


class CustomTheme(Theme):
    class Meta:
        app_label = "admin_interface"
        verbose_name = _("🎨 Theme")
        verbose_name_plural = _("🎨 Themes")

