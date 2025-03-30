from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    qrcode = models.ImageField(
        upload_to='qrcode/',
        blank=True,
        null=True,
    )
    # date_create   -date_create
    def __str__(self):
        return self.name

class Marketplace(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductMarketplace(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace_id = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    url = models.TextField()
