from django import forms
from django.forms import inlineformset_factory

from .models import Product, Marketplace, ProductMarketplaceUrl


class ProductFormCreate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class MarketplaceFormCreate(forms.ModelForm):
    class Meta:
        model = Marketplace
        fields = ['name',]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProductFormUpdate(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description']

class ProductMarketplaceForm(forms.ModelForm):
    class Meta:
        model = ProductMarketplaceUrl
        fields = ['id', 'marketplace_id', 'url']
        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        available_marketplaces = kwargs.pop('available_marketplaces', None)
        super().__init__(*args, **kwargs)

        if available_marketplaces is not None:
            self.fields['marketplace_id'].queryset = available_marketplaces

ProductMarketplaceFormSet = inlineformset_factory(
    Product,
    ProductMarketplaceUrl,
    form=ProductMarketplaceForm,
    fields=('marketplace_id', 'url'),
    extra=3,
    can_delete=True
)