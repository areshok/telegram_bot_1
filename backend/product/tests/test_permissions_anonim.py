import tempfile

from django.test import TestCase, Client, override_settings
from django.urls import reverse


from product.models import Product
from account.models import User


class TestProductPermissionAnonimUser(TestCase):
    # анонимный пользователь
    pass


