from django import forms

from product.models import ProductModel, BrandModel, CategoryModel

from django.utils.safestring import mark_safe

class AdminImageWidget(forms.ClearableFileInput):
    def render(self, name, value, attrs=None, renderer=None):
        html = super().render(name, value, attrs, renderer)
        if value and hasattr(value, "url"):
            html += mark_safe(f'''
                <a href="{value.url}" data-lightbox="image">
                    <img src="{value.url}" height="45px"/>
                </a>''')
        return html


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['image'].label = "📸 Изображение продукта"        


class BrandModelForm(forms.ModelForm):
    class Meta:
        model = BrandModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%;'}),
            'country': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'website': forms.TextInput(attrs={'style': 'width: 100%;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class CategoryModelForm(forms.ModelForm):
    class Meta:
        model = CategoryModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%;'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
