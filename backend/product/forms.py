from django import forms

from .models import Product, Marketplace


class ProductFormCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MarketplaceCreateForm(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }