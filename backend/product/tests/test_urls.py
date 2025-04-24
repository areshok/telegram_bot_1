from django.test import TestCase
from django.urls import reverse


class TestUrlProduct(TestCase):
    "Тест кейс проверки url адресов связанных с моделью product"

    def test_url_product_list(self):
        "тест: проверка url product_list"
        url = reverse('product:product_list')
        self.assertEqual(url, '/product/')

    def test_url_product_detail(self):
        "тест: проверка url product_detail"
        url = reverse('product:product_detail', kwargs={'pk': 1})
        self.assertEqual(url, '/product/1/detail/')

    def test_url_product_create(self):
        "тест: проверка url product_create"
        url = reverse('product:product_create')
        self.assertEqual(url, '/product/create/')

    def test_url_product_update(self):
        "тест: проверка url product_update"
        url = reverse('product:product_update', kwargs={'pk': 1})
        self.assertEqual(url, '/product/1/update/')

    def test_url_product_delete(self):
        "тест: проверка url product_delete"
        url = reverse('product:product_delete', kwargs={'pk': 1})
        self.assertEqual(url, '/product/1/delete/')

    def test_url_product_qrcode_create(self):
        "тест: проверка url qrcode_create"
        url = reverse('product:qrcode_create', kwargs={'pk': 1})
        self.assertEqual(url, '/product/1/qrcode-create/')

    def test_url_product_qrcode_delete(self):
        "тест: проверка url qrcode_delete"
        url = reverse('product:qrcode_delete', kwargs={'pk': 1})
        self.assertEqual(url, '/product/1/qrcode-delete/')

    def test_url_product_qrcode_download(self):
        "тест: проверка url qrcode_download"
        url = reverse('product:qrcode_download', kwargs={'pk': 1})
        self.assertEqual(url, '/product/1/qrcode-download/')


class TestUrlMarketplace(TestCase):
    "Тест кейс прверки url адресов связанных с моделью marketplace"

    def test_url_marketplace_list(self):
        "тест: проверка url marketplace_list"
        url = reverse('product:marketplace_list')
        self.assertEqual(url, '/product/marketplaces/')

    def test_url_marketplace_create(self):
        "тест: проверка url marketplace_create"
        url = reverse('product:marketplace_create')
        self.assertEqual(url, '/product/marketplace/create/')

    def test_url_marketplace_delete(self):
        "тест: проверка url marketplace_delete"
        url = reverse('product:marketplace_delete', kwargs={'pk': 1})
        self.assertEqual(url, '/product/marketplace/1/delete/')
