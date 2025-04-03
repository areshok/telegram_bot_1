# Generated by Django 4.1 on 2025-03-30 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('extend_id', models.PositiveIntegerField(unique=True)),
                ('username', models.CharField(max_length=32)),
                ('first_name', models.CharField(max_length=64)),
                ('last_name', models.CharField(max_length=64, null=True)),
                ('phone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CommentProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('product_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.product')),
                ('telegram_profile_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tgm.telegramprofile')),
            ],
        ),
    ]
