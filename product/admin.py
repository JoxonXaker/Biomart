from django.contrib import admin
from django.utils.safestring import mark_safe

from product.models import CategoryModel, ProductModel, BrandModel, ProductImageModel
from product.forms import ProductModelForm


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'display_logo')


class ProductImageModelTabularInline(admin.TabularInline):
    model = ProductImageModel
    readonly_fields = ['display_image']
    extra = 5
    min_num = 1
    max_num = 5



@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    form = ProductModelForm
    
    # list_display = ('name', 'brand', 'price', 'stock', 'display_image')
    # list_display_links = ('name', 'brand', 'price', 'stock', 'display_image')
    
    inlines = [ProductImageModelTabularInline]
    
    filter_horizontal = ('category',)

    list_display = ('icon_name', 'icon_brand', 'icon_price', 'icon_stock', 'icon_display_image')

    def icon_name(self, obj):
        return obj.name
    icon_name.short_description = "📝 Имя"

    def icon_brand(self, obj):
        return obj.brand
    icon_brand.short_description = "🏷️ Бренд"

    def icon_price(self, obj):
        return obj.price
    icon_price.short_description = "💰 Цена"

    def icon_stock(self, obj):
        return obj.stock
    icon_stock.short_description = "📦 Количество"

    def icon_display_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="45" height="45" />')
        return mark_safe(f'<img src="https://t4.ftcdn.net/jpg/05/21/82/91/360_F_521829166_8Q95OHELrV2GLmhOzStmCO9isNPl5NBy.jpg" width="45" height="45"  style="border: 1px solid #e8e8e8;"/>')
    
    icon_display_image.short_description = "🖼️ Изображение"

