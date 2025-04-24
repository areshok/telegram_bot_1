import tempfile
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse


from product.models import Product, Marketplace
from account.models import User


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.MEDIA_ROOT_TESTS)


class TestProductPermissionAuthUser(TestCase):
    "Тест кейс проверки доступа авторизированного пользователя связанных с моделью product"

    @classmethod
    @override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        User.objects.all().delete()
        Product.objects.all().delete()
        cls.user = User.objects.create_user(
            username='auth_user',
            password='auth_pass'
        )
        Product.objects.create(name='name_1', description='description_1')
        Product.objects.create(name='name_2', description='description_2')
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        Product.objects.all().delete()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        return super().tearDownClass()

    def setUp(self):
        self.client.force_login(self.user)
        return super().setUp()

    def test_post_list_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к product_list"
        response = self.client.get(reverse('product:product_list'))
        self.assertEqual(response.status_code, 200)

    def test_post_detail_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к product_detail"
        product = Product.objects.first()
        response = self.client.get(reverse('product:product_detail', kwargs={'pk': product.id}))
        self.assertEqual(response.status_code, 200)

    def test_product_update_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к product_update"
        product = Product.objects.first()
        response = self.client.get(reverse('product:product_update', kwargs={'pk': product.id}))
        self.assertEqual(response.status_code, 200)

    def test_product_create_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к product_create"
        response = self.client.get(reverse('product:product_create'))
        self.assertEqual(response.status_code, 200)

    def test_product_delete_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к product_delete"
        product = Product.objects.first()
        response = self.client.get(reverse('product:product_delete', kwargs={'pk': product.id}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_qrcode_download_auth_user_access(self):
        """тест: проверка доступа авторизированного пользователя до qrcode_download
        """
        # бля ну я хз, заебал ругаться на 404
        product = Product.objects.first()
        response = self.client.get(reverse('product:qrcode_download', kwargs={'pk': product.id}))
        self.assertEqual(product.qrcode, f'qrcode/{product.id}_{product.name}_qrcode.png')
        self.assertEqual(response.status_code, 200)

    def test_qrcode_create_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к qrcode_create"
        product = Product.objects.first()
        response = self.client.get(reverse('product:qrcode_create', kwargs={'pk': product.id}), follow=True)
        self.assertEqual(response.status_code, 200)

    def test_qrcode_delete_auth_user_access(self):
        "тест: проверка доступа авторизированного пользователя к qrcode_delete"
        product = Product.objects.first()
        response = self.client.get(reverse('product:qrcode_delete', kwargs={'pk': product.id}), follow=True)
        self.assertEqual(response.status_code, 200)


class TestMarketplacePermissionAuthUser(TestCase):
    "Тест кейс проверки доступа авторизированного пользователя связанных с моделью marketplace"

    @classmethod
    def setUpClass(cls):
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        return super().tearDownClass()

    def setUp(self):
        return super().setUp()

    def test_marketplace_list_auth_user_access(self):
        ""
        pass
    def test_marketplace_create_auth_user_access(self):
        ""
        pass
    def test_marketplace_delete_auth_user_access(self):
        ""
        pass
