from django.test import TestCase, Client
from account.models import User
from django.urls import reverse
# Create your tests here.


class ProductTestCase(TestCase):

    def test_template_namespace(self):
        "Проверка шаблонов и namespace на соответсвие"

        template_namespace = {
            'product/product_list.html': reverse('product:product_list'),
            'product/product_update.html': '',
            'product/product_dettail.html': '',
            'product/product_create.html': '',
            'product/marketplace_list': '',
            'product/marketplace_create.html': '',
        }
        pass









