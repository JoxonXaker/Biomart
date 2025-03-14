from django.db import models
from django.utils.safestring import mark_safe


# 1. Dorilar Kategoriyasi modeli
class CategoryModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "♻️ Категории продукта"

    
    def __str__(self):
        return self.name

# 2. Brend modeli
class BrandModel(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)
    logo = models.ImageField(upload_to='brand_logos/', blank=True, null=True)

    class Meta:
        verbose_name = "Бренд"
        verbose_name_plural = "🅱️ Бренды продукта"
    
    def __str__(self):
        return self.name
    
    def display_logo(self):
        if self.logo:
            return mark_safe(f'<img src="{self.logo.url}" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')
        return mark_safe(f'<img src="https://t4.ftcdn.net/jpg/05/21/82/91/360_F_521829166_8Q95OHELrV2GLmhOzStmCO9isNPl5NBy.jpg" width="45" height="45"  style="border: 1px solid #e8e8e8;"/>')

    

# 3. Dori mahsuloti modeli
class ProductModel(models.Model):
    name = models.CharField(max_length=255, help_text="Не более 255 символов")
    category = models.ManyToManyField(CategoryModel, related_name="product")    
    brand = models.ForeignKey(BrandModel, related_name="product", on_delete=models.SET_NULL, null=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Валюта Узбекистан СУМ*")
    stock = models.PositiveIntegerField()
    image = models.ImageField(upload_to='product_images/', blank=True, null=True)
    detail = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "🛍 Продукты"
    
    def __str__(self):
        return self.name
    
    def display_image(self):
        if self.image:
            return mark_safe(f'<img src="{self.image.url}" width="45" height="45" style="border: 1px solid #e8e8e8;"/>')
        # return mark_safe(f'<div style="width: 45px; height: 45px; font-size: 35px">❌</div>')
        return mark_safe(f'<img src="https://t4.ftcdn.net/jpg/05/21/82/91/360_F_521829166_8Q95OHELrV2GLmhOzStmCO9isNPl5NBy.jpg" width="45" height="45"  style="border: 1px solid #e8e8e8;"/>')

class ProductImageModel(models.Model):
    product = models.ForeignKey(ProductModel, related_name='product', on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='product_images/')

    class Meta:
        verbose_name = "Фотографии продукта"
        verbose_name_plural = "Фотографии продукта"

    def __str__(self):
        return f"Image of {self.product.name}"
    
    def display_image(self):
        return mark_safe(f'<img src="{self.image.url}" width="50" height="50" />')