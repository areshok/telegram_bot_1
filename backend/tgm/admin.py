from django.contrib import admin

from .models import TelegramProfile, CommentProduct
# Register your models here.



@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    fields = ('extend_id', 'username')


@admin.register(CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    fields = ('product_id', 'telegram_profile_id')