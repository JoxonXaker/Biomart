from django.db import models
from django.utils.safestring import mark_safe

from imagekit.models import ProcessedImageField
# from imagekit.processors import ResizeToFill

# 1. Carusel modeli
class CarouselItem(models.Model):
    allowed = models.BooleanField(default=False, help_text="С помощью этого поля вы разрешаете сайту публиковать", verbose_name="📢 Разрешить публикацию")
    title = models.CharField(max_length=255, null=True, blank=True, verbose_name="🎠 Названия")
    description = models.TextField(blank=True, null=True, verbose_name="📝 Описание")
    link = models.URLField(blank=True, null=True, verbose_name="🔗 Ссылка")
    image = ProcessedImageField(
        upload_to='carousel/',
        # processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 100},
        null=True,
        verbose_name='📸 Изображение'
    )
    
    class Meta:
        verbose_name = "Карусель"
        verbose_name_plural = "🎠 Карусели"


    def display_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" data-lightbox="image"><img src="{self.image.url}" height="45" style="border: 1px solid #e8e8e8;"/></a>')
        return mark_safe(f'<img src="/media/admin-interface/helper/image.png" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')


    def __str__(self):
        return self.title
