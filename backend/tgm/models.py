from django.db import models

from product.models import Product
from account.models import User


class TelegramProfile(models.Model):
    "Таблица профилей телеграм"
    extend_id = models.PositiveIntegerField(null=False, unique=True)
    username = models.CharField(max_length=32, null=False)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, null=True)

    def __str__(self):
        return self.username


class NotViewedManager(models.Manager):
    "Менеджер для вывода объекто со статусом непросмотренно"
    def get_queryset(self):
        return super().get_queryset().filter(
            status=CommentProduct.Status.NOTVIEWED
        )


class CommentProduct(models.Model):
    "Таблица коментариев"
    class Status(models.TextChoices):
        VIEWED = 'VI', 'Viewed'
        NOTVIEWED = 'NV', 'NotViewed'

    product_id = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_comment'
    )
    telegram_profile_id = models.ForeignKey(
        TelegramProfile,
        on_delete=models.SET_NULL,
        null=True,
        related_name='telegram_comment'
    )
    comment = models.TextField(null=True)
    score = models.IntegerField(null=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.NOTVIEWED
    )
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True,)
    date_create = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
    objects = models.Manager()
    notviewed = NotViewedManager()

    class Meta:
        pass


class MarketingMessage(models.Model):
    "Таблица рекламных сообщений"
    class Status(models.TextChoices):
        "Выбор статуса сообщения"
        OK = "OK", "Completed"
        ER = "ER", "Error"
        EM = "EMPTY", 'Empty'
    name = models.CharField(max_length=100, null=True)
    status = models.CharField(
        max_length=10,
        choices=Status.choices,
        default=Status.EM
    )
    message = models.TextField()
    image = models.ImageField(
        upload_to='marketing/',
        blank=True,
        null=True,
    )
    product_id = models.ForeignKey(
        Product,
        on_delete=models.SET_NULL,
        null=True,
        related_name='product_marketing'
    )
