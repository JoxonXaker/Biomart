from django import forms

from product.models import ProductModel

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
        self.fields['name'].label = "💊 Название продукта"
        self.fields['category'].label = "📂 Категории"
        self.fields['brand'].label = "🏷️ Бренд"
        self.fields['description'].label = "📝 Описание"
        self.fields['price'].label = "💰 Цена"
        self.fields['stock'].label = "📦 Количество на складе"
        self.fields['detail'].label = "🛠 Подробный"
        self.fields['image'].label = "📸 Изображение продукта"        
