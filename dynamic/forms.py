from django import forms

from dynamic.models import CarouselItem




class CarouselModelForm(forms.ModelForm):
    class Meta:
        model = CarouselItem
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'style': 'width: 100%;'}),
            'description': forms.Textarea(attrs={'style': 'width: 100%;'}),
        }


