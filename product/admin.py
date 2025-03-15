from django.contrib import admin
from django.utils.safestring import mark_safe


from product.models import CategoryModel, ProductModel, BrandModel, ProductImageModel
from product.forms import ProductModelForm, BrandModelForm, CategoryModelForm


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    # list_display = ('name', 'description')
    # summernote_fields = ('description',)

    form = CategoryModelForm

    list_display = ('icon_name', 'icon_description')
    list_display_links = ('icon_name', 'icon_description')

    def icon_name(self, obj):
        return obj.name
    
    def icon_description(self, obj):
        return obj.description
    icon_description.short_description = "🏷️ Бренд"
    

    icon_name.short_description = "📝 Имя Бренд"



@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    form = BrandModelForm
    readonly_fields = ('display_logo',)


    list_display = ('id', 'icon_name', 'icon_display_image')
    list_display_links = ('id', 'icon_name', )

    def icon_name(self, obj):
        return obj.name
    icon_name.short_description = "📝 Имя Бренд"

    def icon_display_image(self, obj):
        return obj.display_logo()
        
    icon_display_image.short_description = "🖼️ Изображение"


class ProductImageModelTabularInline(admin.TabularInline):
    model = ProductImageModel
    readonly_fields = ['display_image']
    extra = 5
    min_num = 1
    max_num = 5



@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    form = ProductModelForm
    
    inlines = [ProductImageModelTabularInline]

    filter_horizontal = ('category',)

    list_display = ('icon_name', 'icon_brand', 'icon_price', 'icon_stock', 'icon_display_image')
    list_display_links = ('icon_name', 'icon_brand', 'icon_price', 'icon_stock')

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
        return obj.display_image()
        
    icon_display_image.short_description = "🖼️ Изображение"

