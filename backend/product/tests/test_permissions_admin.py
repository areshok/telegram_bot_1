import tempfile
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse


from product.models import Product, Marketplace
from account.models import User

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.MEDIA_ROOT_TESTS)


class TestProductPermissionAdminUser(TestCase):
    "Тест кейс проверки доступа от админа связанных с моделью product"

    @classmethod
    @override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        User.objects.all().delete()
        cls.admin = User.objects.create_superuser(
            username='test_admin',
            password='test_admin_pass'
        )
        Product.objects.create(name='test1', description='test1')
        Product.objects.create(name='test2', description='test2')
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        Product.objects.all().delete()
        User.objects.all().delete()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        return super().tearDownClass()

    def setUp(self):
        self.client.force_login(self.admin)
        return super().setUp()

    def test_post_list_admin_user_access(self):
        "тест: проверка доступа админа до post_list"
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_admin_user_access(self):
        "тест: проверка доступа админа до post_detail"
        product = Product.objects.first()
        response = self.client.get(reverse("product:product_detail", kwargs={"pk": product.id}))
        self.assertEqual(response.status_code, 200)

    def test_product_update_admin_user_access(self):
        "тест: проверка доступа админа до product_update"
        product = Product.objects.first()
        response = self.client.get(reverse('product:product_update', kwargs={'pk': product.id}))
        self.assertEqual(response.status_code, 200)

    def test_product_create_admin_user_access(self):
        "тест: проверка доступа админа до product_create"
        response = self.client.get(reverse('product:product_create'))
        self.assertEqual(response.status_code, 200)

    def test_product_delete_admin_user_access(self):
        "тест: проверка доступа админа до product_delete"
        product = Product.objects.first()
        response = self.client.get(reverse('product:product_delete', kwargs={'pk': product.id}))
        self.assertEqual(response.status_code, 200)

    def test_qrcode_download_admin_user_access(self):
        "тест: проверка доступа админа до qrcode_download"
        # бля ну я хз, заебал ругаться на 404
        product = Product.objects.first()
        response = self.client.get(reverse('product:qrcode_download', kwargs={'pk': product.id}))
        self.assertEqual(product.qrcode, f'qrcode/{product.id}_{product.name}_qrcode.png')
        self.assertEqual(response.status_code, 200)

    def test_qrcode_create_admin_user_access(self):
        "тест: проверка доступа админа до qrcode_create"
        product = Product.objects.first()
        response = self.client.get(reverse('product:qrcode_create', kwargs={'pk': product.id}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_qrcode_delete_admin_user_access(self):
        "тест: проверка доступа админа до qrcode_delete"
        product = Product.objects.create(name='test_3', description='test_3')
        response = self.client.get(reverse('product:qrcode_delete', kwargs={'pk': product.id}), follow=True)
        self.assertEqual(response.status_code, 200)


class TestMarketplacePermissionAdminUser(TestCase):
    "Тест кейс проверки доступа от админа связанных с моделью marketplace"

    @classmethod
    @override_settings(MEDIA_ROOT=tempfile.gettempdir())
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        User.objects.all().delete()
        cls.admin = User.objects.create_superuser(
            username='test_admin',
            password='test_admin_pass'
        )
        Marketplace.objects.create(name='test_market')
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        cls.temp_media.cleanup()
        return super().tearDownClass()

    def setUp(self):
        self.client.force_login(self.admin)
        return super().setUp()

    def test_marketplace_list_admin_user_access(self):
        "тест: проверка доступа админа до marketplace_list"
        response = self.client.get(reverse('product:marketplace_list'))
        self.assertEqual(response.status_code, 200)

    def test_marketplace_create_admin_user_access(self):
        "тест: проверка доступа админа до create_marketplace"
        response = self.client.get(reverse('product:marketplace_create'))
        self.assertEqual(response.status_code, 200)

    def test_marketplace_delete_admin_user_access(self):
        "тест: проверка доступа админа до marketplace_delete"
        marketplace = Marketplace.objects.create(name='test_2')
        response = self.client.get(reverse('product:marketplace_delete', kwargs={'pk': marketplace.id}), follow=True)
        self.assertEqual(response.status_code, 200)
