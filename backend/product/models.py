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


class ProductMarketplace(models.Model):
    "Таблица ссылок товаров на маркетлейсах"

    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace_id = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    url = models.URLField(
        verbose_name='ссылка на маркетплейс',
    )
