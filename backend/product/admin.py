from django.contrib import admin

# Register your models here.
from .models import Product, ProductMarketplace



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name',)

@admin.register(ProductMarketplace)
class ProductMarketplaceAdmin(admin.ModelAdmin):
    fields = ['product_id','marketplace_id', 'url']
