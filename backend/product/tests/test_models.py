import tempfile
import shutil

from django.conf import settings
from django.test import TestCase, override_settings

from product.models import Product, Marketplace


TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.MEDIA_ROOT_TESTS)

class TestProductModel(TestCase):
    "Тест кейс проверки модели Product"

    @classmethod
    @override_settings(MEDIA_ROOT=TEMP_MEDIA_ROOT)
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        Product.objects.all().delete()
        Product.objects.create(
            name='product_name',
            description='product_description'
        )
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        Product.objects.all().delete()
        return super().tearDownClass()

    def test_signal_create_qrcode(self):
        """тест: проверка атоматического создание
        qrcode при создании объекта"""
        product = Product.objects.first()
        self.assertEqual(product.qrcode, f'qrcode/{product.id}_{product.name}_qrcode.png')









