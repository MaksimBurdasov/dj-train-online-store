from .models import Product
from django.forms import ModelForm, TextInput, Textarea, DecimalField


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["title", "description", "price"]
        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Как называется?'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Добавьте описание.'
            })
        }