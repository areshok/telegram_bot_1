import tempfile
from django.test import TestCase, Client, override_settings
from account.models import User
from django.urls import reverse

# Create your tests here.

from account.models import User
from .models import Product


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

    def test_template(self):
        "тест: проверка шаблона"
        response = self.client.get('/product/')
        self.assertTemplateUsed(response, 'product/product_list.html')

    def test_name_to_url(self):
        "тест: проверка сопоставление namespace и url"
        url = reverse('product:product_list')
        self.assertEqual(url, '/product/')

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

    def test_pagination_unknown_page(self):
        "тест: пагинации неизветной страницы"
        response = self.client.get(reverse('product:product_list') + '?page=999')
        self.assertEqual(response.status_code, 404)

    def test_permission_authorized_user(self):
        "тест: проверка доступа авторизированного пользователя"
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)

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

    @classmethod
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        cls.temp_media.cleanup()
        super().tearDownClass()

    def setUp(self):
        Product.objects.create(
            name='name_test',
            description='description_test'
        )
        self.anonim = Client()
        User.objects.create_user(
            username='test_user',
            password='Test_password'
        )
        logged = self.client.login(
            username='test_user',
            password='Test_password'
        )
        if not logged:
            raise ValueError("Не удалось войти в систему")

    def tearDown(self):
        Product.objects.all().delete()

    def test_template(self):
        "тест: проверка шаблона"
        response = self.client.get('/product/detail/1/')
        self.assertTemplateUsed(response, 'product/product_detail.html')

    def test_name_to_url(self):
        "тест: проверка сопоставление namespace и url"
        product = Product.objects.first()
        url = reverse('product:product_detail', kwargs={'pk': product.id})
        self.assertEqual(url, '/product/detail/1/')

    def test_context(self):
        ''
        self.fail('Не сделанно')

    def test_permission_authorized_user(self):
        "тест: проверка доступа авторизированного пользователя"
        product = Product.objects.first()
        response = self.client.get(reverse('product:product_detail', kwargs={'pk': product.id}))
        self.assertEqual(response.status_code, 200)

    def test_permission_anonymous_user(self):
        """тест: проверка доступа неавторизированного пользователя.
        Перенаправляется на страницу входа."""
        product = Product.objects.first()
        anonim = Client()
        response = anonim.get(
            reverse('product:product_detail', kwargs={'pk': product.id})
        )
        self.assertEqual(response.status_code, 302)


class ProductCreateTest(TestCase):
    "тест кейс product_create"

    def setUp(self):
        User.objects.create_user(
                username='test_user',
                password='Test_password'
            )
        logged = self.client.login(
                username='test_user',
                password='Test_password'
            )
        if not logged:
            raise ValueError("Не удалось войти в систему")

    def tearDown(self):
        Product.objects.all().delete()

    def test_template(self):
        "Тест: проверка шаблона"
        response = self.client.get(reverse('product:product_create'))
        self.assertTemplateUsed(response, 'product/product_create.html')
        #self.fail('Не сделанно')

    def test_context(self):
        ''
        self.fail('Не сделанно')

    def test_permission(self):
        ''
        self.fail('Не сделанно')

'''
class ProductUpdateTest(TestCase):
    ''

    def test_template(self):
        ''
        self.fail('Не сделанно')

    def test_context(self):
        ''
        self.fail('Не сделанно')

    def test_permission(self):
        ''
        self.fail('Не сделанно')


class ProductDeleteTest(TestCase):
    ''

    def test_template(self):
        ''
        self.fail('Не сделанно')

    def test_context(self):
        ''
        self.fail('Не сделанно')

    def test_permission(self):
        ''
        self.fail('Не сделанно')

'''

class ProductModelTest(TestCase):
    pass