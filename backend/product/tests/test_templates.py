import tempfile

from django.test import TestCase, override_settings
from django.urls import reverse

from account.models import User
from product.models import Product, Marketplace


class TestProductTemplate(TestCase):
    "Тест кейс проверки шаблонов приложения связанные с моделью product"

    @classmethod
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUpClass(cls):
        "Установка"
        cls.temp_media = tempfile.TemporaryDirectory()
        Product.objects.create(
            name='name_1',
            description='description_1'
        )
        User.objects.all().delete()
        User.objects.create_user(
            username='test',
            password='test'
        )
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        "Удаление"
        cls.temp_media.cleanup()
        Product.objects.all().delete()
        User.objects.all().delete()
        super().tearDownClass()

    def setUp(self):
        self.client.login(
            username='test',
            password='test'
        )

    def test_product_list_template(self):
        "тест: проверка шаблона product_list"
        response = self.client.get(reverse('product:product_list'))
        self.assertTemplateUsed(response, 'product/product_list.html')

    def test_product_detail_template(self):
        "тест: проверка шаблона product_detail"
        product = Product.objects.first()
        url = reverse('product:product_detail', kwargs={'pk': product.id})
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'product/product_detail.html')

    def test_product_create_template(self):
        "тест: проверка шаблона product_create"
        response = self.client.get(reverse('product:product_create'))
        self.assertTemplateUsed(response, 'product/product_create.html')

    def test_product_update_template(self):
        "тест: проверка шаблона product_update"
        product = Product.objects.first()
        response = self.client.get(
            reverse('product:product_update', kwargs={'pk': product.id})
        )
        self.assertTemplateUsed(response, 'product/product_update.html')


class TestMarketplaceTemplate(TestCase):
    """Тест кейс проверки шаблонов приложения связанные с моделью marketplace.
        Доступ только у администраторов.
    """

    @classmethod
    def setUpClass(cls):
        "Установка"
        Marketplace.objects.create(name='test')
        User.objects.all().delete()
        User.objects.create_superuser(
            username='test',
            password='test'
        )
        super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        "Удаление"
        Marketplace.objects.all().delete()
        User.objects.all().delete()
        super().tearDownClass()

    def setUp(self):
        self.client.login(
            username='test',
            password='test'
        )

    def test_marketplace_list_template(self):
        "тест: проверка шаблона marketplace_list"
        response = self.client.get(reverse('product:marketplace_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'product/marketplace_list.html')

    def test_marketplace_create_template(self):
        "тест: проверка шаблона marketplace_create"
        response = self.client.get(reverse('product:marketplace_create'))
        self.assertTemplateUsed(response, 'product/marketplace_create.html')
