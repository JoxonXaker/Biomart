from django.contrib import admin
from django.contrib.auth.models import User, Group


User._meta.verbose_name = "👤 Пользователь"
User._meta.verbose_name_plural = "👥 Пользователи"

Group._meta.verbose_name = "🛡 Группа"
Group._meta.verbose_name_plural = "🛡 Группы"


    

