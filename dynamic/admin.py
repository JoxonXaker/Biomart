from django.contrib import admin
from django.utils.safestring import mark_safe

from dynamic.models import CarouselItem
from dynamic.forms import CarouselModelForm

@admin.register(CarouselItem)
class CarouselModelAdmin(admin.ModelAdmin):
    form = CarouselModelForm

    list_display = ('id', 'title', 'display_image', 'allowed')
    list_display_links = ('id','title', )
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
