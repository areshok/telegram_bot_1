from django.db import models
from .validation import MinCharacterValidator


class Product(models.Model):
    "Таблица товаров"

    name = models.CharField(
        max_length=250,
        validators=[MinCharacterValidator(2),],
        verbose_name='название товара'
    )
    description = models.TextField(
        validators=[MinCharacterValidator(2)],
        verbose_name='описание товара',
    )
    qrcode = models.ImageField(
        upload_to='qrcode/',
        blank=True,
        null=True,
    )
    date_create = models.DateTimeField(
        auto_now_add=True,
        verbose_name='дата создания'
        )

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name


class Marketplace(models.Model):
    "Таблица маркетплейсов"

    name = models.CharField(
        max_length=100,
        validators=[MinCharacterValidator(2)],
        verbose_name='название маркетплейса',
        )

    def __str__(self):
        return self.name


class ProductMarketplaceUrl(models.Model):
    "Таблица ссылок товаров на маркетлейсах"

    product_id = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='product_url'
    )
    marketplace_id = models.ForeignKey(
        Marketplace, on_delete=models.CASCADE, related_name='marketplace_url')
    url = models.URLField(
        verbose_name='ссылка на маркетплейс',
    )

    class Meta:
        unique_together = [['product_id', 'marketplace_id']]

    def __str__(self):
        return f'{self.product_id} - {self.marketplace_id} - {self.url}'
