from django.contrib import admin

# Register your models here.
from .models import Product, ProductMarketplaceUrl, Marketplace



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', ]
    list_display = ['id', 'name']

@admin.register(ProductMarketplaceUrl)
class ProductMarketplaceAdmin(admin.ModelAdmin):
    fields = ['product_id','marketplace_id', 'url']

@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    fields = ['name',]