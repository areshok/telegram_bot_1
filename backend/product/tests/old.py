import tempfile
from django.test import TestCase, Client, override_settings
from account.models import User
from django.urls import reverse

# Create your tests here.

from account.models import User
from ..models import Product


MAX_COUNT = 15


class ProductListTest(TestCase):
    "Тест кейст product_list"

    @classmethod
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        for i in range(1,MAX_COUNT + 1):
            Product.objects.create(
                name=f'name_{i}',
                description=f'description_{i}'
            )
        cls.anonim = Client()
        cls.user = User.objects.create_user(
            username='test_user',
            password='Test_password'
        )
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.temp_media.cleanup()
        cls.anonim = None
        cls.user.delete()
        Product.objects.all().delete()
        super().tearDownClass()

    def setUp(self):
        logged = self.client.login(
            username='test_user',
            password='Test_password'
        )
        if not logged:
            raise ValueError("Не удалось войти в систему")


    def test_context(self):
        "тест: проверка отображения товаров на странице"
        response = self.client.get(reverse('product:product_list'))
        products = response.context['page_obj']
        self.assertIn('name', products[0].name)
        self.assertIn('description', products[0].description)

    def test_pagination_first_page(self):
        "тест: проверка пагинации первой страницы"
        response = self.client.get(reverse('product:product_list'))
        self.assertTrue('is_paginated' in response.context)
        page_obj = response.context['page_obj']
        self.assertEqual(len(page_obj), 10)

    def test_pagination_second_page(self):
        "тест: проверка пагинации второй страницы"
        response = self.client.get(reverse('product:product_list') + '?page=2')
        self.assertTrue('is_paginated' in response.context)
        page_obj = response.context['page_obj']
        self.assertEqual(len(page_obj), 5)



    def test_permission_anonymous_user(self):
        """тест: проверка доступа неавторизированного пользователя.
        Перенаправляется на страницу входа."""
        response = self.anonim.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 302)

    def test_ordering(self):
        "тест: проверка сортировки"
        response = self.client.get(reverse('product:product_list'))
        products = response.context['page_obj']
        self.assertEqual(products[0].name, f'name_{MAX_COUNT}')
        self.assertEqual(products[0].description, f'description_{MAX_COUNT}')


class ProductDetailTest(TestCase):
    "Тест кейс product_detail"

    def setUp(self):
        self.anonim = Client()


    def test_permission_anonymous_user(self):
        """тест: проверка доступа неавторизированного пользователя.
        Перенаправляется на страницу входа."""
        product = Product.objects.first()
        anonim = Client()
        response = anonim.get(
            reverse('product:product_detail', kwargs={'pk': product.id})
        )
        self.assertEqual(response.status_code, 302)




