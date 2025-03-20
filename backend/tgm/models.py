from django.db import models

from product.models import Product
# Create your models here.


class TelegramProfile(models.Model):
    extend_id = models.PositiveIntegerField(null=False, unique=True)
    username = models.CharField(max_length=32, null=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True)
    phone = models.CharField(max_length=15)


class CommentProduct(models.Model):
    product_id = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True
    )
    telegram_profile_id = models.ForeignKey(
        TelegramProfile,
        on_delete=models.SET_NULL,
        null=True
    )
    comment = models.TextField()


