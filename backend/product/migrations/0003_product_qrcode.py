# Generated by Django 4.1 on 2025-03-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_marketplace_productmarketplace'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='qrcode',
            field=models.ImageField(blank=True, null=True, upload_to='qrcode/'),
        ),
    ]
