from django.contrib import admin

from .models import TelegramProfile, CommentProduct, MarketingMessage
# Register your models here.



@admin.register(TelegramProfile)
class TelegramProfileAdmin(admin.ModelAdmin):
    fields = ('extend_id', 'username')


@admin.register(CommentProduct)
class CommentProductAdmin(admin.ModelAdmin):
    fields = ('product_id', 'telegram_profile_id', 'comment', 'score')
    list_display = ['product_id', 'telegram_profile_id', 'comment', 'score']


@admin.register(MarketingMessage)
class MarketingMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'message', 'product_id')
    fields = ['name', 'status', 'message', 'product_id']