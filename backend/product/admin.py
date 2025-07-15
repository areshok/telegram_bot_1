from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
# Register your models here.
from .models import Product, ProductMarketplaceUrl, Marketplace

from .views import QrcodeDelete


class ProductMarketplaceInLine(admin.TabularInline):
    model = ProductMarketplaceUrl
    extra = 1
    fields = ("marketplace_id", "url")

    def has_add_permission(self, request, obj=None):
        return request.user.is_staff

    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductMarketplaceInLine]
    fields = ['name', 'description']
    list_display = [
        'name',
        'description',
        "qrcode_status",
        "qrcode_delete",
        "qrcode_download"
    ]

    def history_view(self, request, object_id, extra_context=None):
        if not request.user.is_superuser:
            from django.core.exceptions import PermissionDenied
            raise PermissionDenied
        return super().history_view(request, object_id, extra_context)

    @admin.display(description="Удалить Qrcode")
    def qrcode_delete(self, obj):
        "добавление кнопки в для каждого объекта"
        return format_html(
            '<a class="button" href="{}">Удалить</a>',
            reverse("product:qrcode_delete", args=[obj.pk])
        )

    @admin.display(description="Скачать")
    def qrcode_download(self, obj):
        return format_html(
            '<a class="button" href="{}">Скачать</a>',
            reverse("product:qrcode_download", args=[obj.pk])
        )

    @admin.display(description="Qrcode")
    def qrcode_status(self, obj):
        if obj.qrcode:
            return True
        else:
            return False

    qrcode_status.boolean = True


@admin.register(ProductMarketplaceUrl)
class ProductMarketplaceAdmin(admin.ModelAdmin):
    fields = ['product_id','marketplace_id', 'url']

    def has_module_permission(self, request):
        return request.user.is_superuser

    def has_view_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_add_permission(self, request):
        return request.user.is_superuser

    def has_change_permission(self, request, obj=None):
        return request.user.is_superuser

    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser

@admin.register(Marketplace)
class MarketplaceAdmin(admin.ModelAdmin):
    fields = ['name',]