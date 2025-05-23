# Generated by Django 4.1 on 2025-04-25 08:16

from django.db import migrations, models
import django.db.models.deletion
import product.validation


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MarketingMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('OK', 'Completed'), ('ER', 'Error'), ('EMPTY', 'Empty')], default='EMPTY', max_length=10)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='marketing/')),
            ],
        ),
        migrations.CreateModel(
            name='Marketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, validators=[product.validation.MinCharacterValidator(2, meassage='Значение не может быть меньше 2 символов.')], verbose_name='название маркетплейса')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, validators=[product.validation.MinCharacterValidator(2, meassage='Значение не может быть меньше 2 символов.')], verbose_name='название товара')),
                ('description', models.TextField(validators=[product.validation.MinCharacterValidator(2, meassage='Значение не может быть меньше 2 символов.')], verbose_name='описание товара')),
                ('qrcode', models.ImageField(blank=True, null=True, upload_to='qrcode/')),
                ('date_create', models.DateTimeField(auto_now_add=True, verbose_name='дата создания')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ProductMarketplace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='ссылка на маркетплейс')),
                ('marketplace_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.marketplace')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
            options={
                'unique_together': {('product_id', 'marketplace_id')},
            },
        ),
    ]
