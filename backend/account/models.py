from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, User, Permission

from product.models import Product


@receiver(pre_save, sender=User)
def set_staff_status(sender, instance, **kwargs):
    if not instance.pk:
        instance.is_staff = True

@receiver(post_save, sender=User)
def add_permission_user(sender, instance, created, **kwargs):
    if created and instance.is_staff:
        permissions = Permission.objects.filter(
            codename__in=[
                "change_product", "view_product",
                "view_productmarketplaceurl", "change_productmarketplaceurl"
            ]
        )
        instance.user_permissions.add(*permissions)
