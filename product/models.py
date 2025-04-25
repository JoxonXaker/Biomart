from django.db import models
from django_quill.fields import QuillField
from django.utils.safestring import mark_safe

from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill


# 1. Dorilar Kategoriyasi modeli
class CategoryModel(models.Model):
    allowed = models.BooleanField(default=False, help_text="С помощью этого поля вы разрешаете сайту публиковать", verbose_name="📢 Разрешить публикацию")
    name = models.CharField(max_length=100, unique=True, verbose_name="♻️ Название бренда")
    description = models.TextField(blank=True, null=True, verbose_name="📝 Описание")
    image = ProcessedImageField(
        upload_to='category_images/',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 100},
        null=True
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "♻️ Категории продукта"
    
    def __str__(self):
        return self.name
    
    def display_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" data-lightbox="image"><img src="{self.image.url}" width="45" height="45" style="border: 1px solid #e8e8e8;"/></a>')
        return mark_safe(f'<img src="/media/admin-interface/helper/image.png" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')



# 2. Brend modeli
class BrandModel(models.Model):
    allowed = models.BooleanField(default=False, help_text="С помощью этого поля вы разрешаете сайту публиковать", verbose_name="📢 Разрешить публикацию")
    name = models.CharField(max_length=100, unique=True, verbose_name="🏷️ Название бренда")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="🌍 Страна-производитель")
    website = models.URLField(blank=True, null=True, verbose_name="🔗 Веб-сайт")
    description = QuillField(blank=True, null=True, verbose_name="🔍 Подробный")
    logo = ProcessedImageField(
        upload_to='brand_logos/',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True,
        verbose_name="🎨 Логотип"
    )
    
    class Meta:
        verbose_name = "🅱 Бренд"
        verbose_name_plural = "🅱 Бренды продукта"
    
    def __str__(self):
        return self.name
    
    def display_logo(self):
        if self.logo:
            return mark_safe(f'<a href="{self.logo.url}" data-lightbox="image"><img src="{self.logo.url}" width="45" height="45" style="border: 1px solid #e8e8e8;"/></a>')
        return mark_safe(f'<img src="/media/admin-interface/helper/image.png" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')


# 3. Dori mahsuloti modeli
class ProductModel(models.Model):
    allowed = models.BooleanField(default=False, help_text="С помощью этого поля вы разрешаете сайту публиковать", verbose_name="📢 Разрешить")
    name = models.CharField(max_length=255, help_text="Не более 255 символов", verbose_name="💊 Название продукта")
    category = models.ManyToManyField(CategoryModel, related_name="product_category", verbose_name="📂 Категории")    
    brand = models.ForeignKey(BrandModel, related_name="product_brand", on_delete=models.SET_NULL, null=True, verbose_name="🏷️ Бренд")
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name="📝 Описание")
    detail = QuillField(null=True, blank=True, verbose_name="🛠 Подробный")
    image = ProcessedImageField(
        upload_to='product_images/',
        processors=[ResizeToFill(250, 250)],
        format='JPEG',
        options={'quality': 100},
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "🛍 Продукты"
    
    def __str__(self):
        return self.name
    
    def display_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" data-lightbox="image"><img src="{self.image.url}" width="45" height="45" style="border: 1px solid #e8e8e8;"/></a>')
        return mark_safe(f'<img src="/media/admin-interface/helper/image.png" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')



# Product-ni rasmlar modeli
class ProductImageModel(models.Model):
    allowed = models.BooleanField(default=False, help_text="С помощью этого поля вы разрешаете сайту публиковать", verbose_name="📢 Разрешить")
    product = models.ForeignKey(ProductModel, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', verbose_name='📸 Изображение')

    class Meta:
        verbose_name = "Фотографии продукта"
        verbose_name_plural = "📸 Фотографии продукта"

    def __str__(self):
        return f"Image of {self.product.name}"
    
    def display_image(self):
        if self.image:
            return mark_safe(f'<a href="{self.image.url}" data-lightbox="gallery"><img src="{self.image.url}" width="45" height="45" style="border: 1px solid #e8e8e8;"/></a>')
        return mark_safe(f'<img src="/media/admin-interface/helper/image.png" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')
    

# Productni bir-nechta o`lchamli modeli
class ProductVariantsModel(models.Model):
    allowed = models.BooleanField(default=False, help_text="С помощью этого поля вы разрешаете сайту публиковать", verbose_name="📢 Разрешить")
    product = models.ForeignKey(ProductModel, related_name='variants', on_delete=models.CASCADE)
    package_quantity = models.CharField(max_length=25, help_text="Не более 25 символов", verbose_name="🧺 Количество в упаковке")
    product_code = models.CharField(max_length=25, help_text="Не более 25 символов", null=True, blank=True, verbose_name="🏷️ Код товара")
    shipping_weight = models.CharField(max_length=25, help_text="Не более 25 символов", null=True, blank=True, verbose_name="⚖️	Вес при доставке")
    dimensions = models.CharField(max_length=25, help_text="Не более 25 символов", null=True, blank=True, verbose_name="📐 Размеры")
    price = models.DecimalField(max_digits=10, decimal_places=0, help_text="Валюта Узбекистан СУМ*", verbose_name="💸 Цена")
    stock = models.PositiveIntegerField(verbose_name="📦 В наличии")

    class Meta: 
        verbose_name = "Количество в упаковке"
        verbose_name_plural = "Количество в упаковке"

    def __str__(self):
        return self.product.name
    

CategoryModel.display_image.short_description = "🖼️ Просмотр изображения"
BrandModel.display_logo.short_description = "🎨 Внешний вид логотипа"
ProductImageModel.display_image.short_description = "🖼️ Просмотр изображения"
ProductModel.display_image.short_description = "🖼️ Просмотр изображения"