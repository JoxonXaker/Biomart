from django.contrib import admin
from django.utils.safestring import mark_safe


from product.models import CategoryModel, ProductModel, BrandModel, ProductImageModel, ProductVariantsModel
from product.forms import ProductModelForm, BrandModelForm, CategoryModelForm


@admin.register(CategoryModel)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryModelForm

    list_display = ('id', 'name', 'display_image', 'allowed')
    list_display_links = ('id','name', )
    list_editable = ('allowed',)
    readonly_fields = ('display_image',)


    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css',)
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js',)


    def icon_display_image(self, obj):
        return obj.display_image()
        
    icon_display_image.short_description = "🖼️ Изображение"
    


@admin.register(BrandModel)
class BrandAdmin(admin.ModelAdmin):
    form = BrandModelForm
    readonly_fields = ('display_logo',)

    list_display = ('id', 'name', 'icon_display_image', 'allowed')
    list_display_links = ('id', 'name', )

    list_editable = ('allowed',)

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css',)
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js',)

    def icon_display_image(self, obj):
        return obj.display_logo()
        
    icon_display_image.short_description = "🖼️ Изображение"


class ProductImageModelTabularInline(admin.TabularInline):
    model = ProductImageModel
    readonly_fields = ['display_image']
    # extra = 5
    min_num = 1
    max_num = 5

class ProductVariantModelTabularInline(admin.TabularInline):
    model = ProductVariantsModel
    # extra = 5
    min_num = 1
    max_num = 5

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    form = ProductModelForm
    readonly_fields = ('display_image',)
    
    inlines = [ProductVariantModelTabularInline, ProductImageModelTabularInline]

    filter_horizontal = ('category',)

    list_display = ('name', 'brand', 'icon_display_image', 'allowed')
    list_display_links = ('name', 'brand', )

    list_editable = ['allowed',]

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css',)
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js',)


    def icon_display_image(self, obj):
        return obj.display_image()
        
    icon_display_image.short_description = "🖼️ Изображение"

