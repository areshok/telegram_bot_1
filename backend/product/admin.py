from django.contrib import admin

# Register your models here.
from .models import Product



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ('name',)
