from django.contrib import admin
from .models import OrderModel, OrderItemModel
from django.utils.safestring import mark_safe



class OrderItemInline(admin.TabularInline):
    model = OrderItemModel
    extra = 0
    readonly_fields = (
        'product_name', 'package_quantity', 'price', 'quantity',
        'display_product_image', 'total_price'
    )
    fields = (
        'product_name', 'package_quantity', 'quantity', 'price', 'total_price', 'display_product_image'
    )
    can_delete = False
    
    
    def display_product_image(self, obj):
        return obj.display_image()

    class Media:
        css = {
            'all': ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/css/lightbox.min.css',)
        }
        js = ('https://cdnjs.cloudflare.com/ajax/libs/lightbox2/2.11.3/js/lightbox.min.js',)

    display_product_image.short_description = "🖼️ Картинка"

    def total_price(self, obj):
        return obj.total_price()
    total_price.short_description = "💰 Сумма"


@admin.register(OrderModel)
class OrderModelAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'name', 'phone', 'delivery', 'status', 'date', 'total_price_display'
    )
    list_display_links = ('id', 'name', 'phone', 'delivery', 'date', 'total_price_display')
    list_filter = ('status', 'delivery', 'date')
    list_editable = ('status',)
    ordering = ('-date',)
    inlines = [OrderItemInline]
    

    # ✅ Bu yerga qo‘shamiz
    readonly_fields = ('name', 'address', 'comment', 'phone', 'delivery', 'date', 'total_price_display', 'total_items_price_display', 'delivery', 'delivery_price')

    fieldsets = (
        ("📦 Заказчик", {
            'fields': ('name', 'phone', 'address', 'comment')
        }),
        ("🚚 Доставка", {
            'fields': ('delivery', 'delivery_price')
        }),
        ("🕒 Время и статус", {
            'fields': ('status', 'date', 'total_items_price_display','total_price_display')
        }),
    )

    def total_price_display(self, obj):
        return f"{obj.total_price():,}".replace(",", " ") + " сум"
    total_price_display.short_description = "💰 Общая сумма"

    def total_items_price_display(self, obj):
        return f"{obj.total_items_price():,}".replace(",", " ") + " сум"
    total_items_price_display.short_description = "📦 Общая сумма продукта"

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return True

    def has_delete_permission(self, request, obj=None):
        return True



# @admin.register(OrderItemModel)
# class OrderItemModelAdmin(admin.ModelAdmin):
#     list_display = ('order', 'product_name', 'package_quantity', 'price', 'quantity')
#     readonly_fields = (
#         'order', 'product_name', 'package_quantity', 'price', 'quantity',
#         'product_image', 'variant_id', 'product_id'
#     )

#     def product_image(self, obj):
#         if obj.product_image:
#             return f'<img src="{obj.product_image}" width="80" />'
#         return "—"
#     product_image.allow_tags = True
#     product_image.short_description = "🖼️ Изображение"
