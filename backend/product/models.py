from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()


class Marketplace(models.Model):
    name = models.CharField(max_length=100)

class ProductMarketplace(models.Model):
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    marketplace_id = models.ForeignKey(Marketplace, on_delete=models.CASCADE)
    url = models.TextField()

