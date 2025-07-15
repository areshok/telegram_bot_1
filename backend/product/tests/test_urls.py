import allure
from django.urls import reverse


class TestCaseUrlProduct:

    @allure.title("тест: проверка url product_list")
    def test_url_product_list(self):
        "тест: проверка url product_list"
        url = reverse('product:product_list')
        assert url == '/product/'

    @allure.title("тест: проверка url product_detail")
    def test_url_product_detail(self):
        "тест: проверка url product_detail"
        url = reverse('product:product_detail', kwargs={'pk': 1})
        assert url == '/product/1/detail/'

    @allure.title("тест: проверка url product_create")
    def test_url_product_create(self):
        "тест: проверка url product_create"
        url = reverse('product:product_create')
        assert url == '/product/create/'

    @allure.title("тест: проверка url product_update")
    def test_url_product_update(self):
        "тест: проверка url product_update"
        url = reverse('product:product_update', kwargs={'pk': 1})
        assert url == '/product/1/update/'

    @allure.title("тест: проверка url product_delete")
    def test_url_product_delete(self):
        "тест: проверка url product_delete"
        url = reverse('product:product_delete', kwargs={'pk': 1})
        assert url == '/product/1/delete/'

    @allure.title("тест: проверка url qrcode_create")
    def test_url_product_qrcode_create(self):
        "тест: проверка url qrcode_create"
        url = reverse('product:qrcode_create', kwargs={'pk': 1})
        assert url == '/product/1/qrcode-create/'

    @allure.title("тест: проверка url qrcode_delete")
    def test_url_product_qrcode_delete(self):
        "тест: проверка url qrcode_delete"
        url = reverse('product:qrcode_delete', kwargs={'pk': 1})
        assert url == '/product/1/qrcode-delete/'

    @allure.title("тест: проверка url qrcode_download")
    def test_url_product_qrcode_download(self):
        "тест: проверка url qrcode_download"
        url = reverse('product:qrcode_download', kwargs={'pk': 1})
        assert url == '/product/1/qrcode-download/'


class TestCaseUrlMarketplace:
    "Тест кейс прверки url адресов связанных с моделью marketplace"

    @allure.title("тест: проверка url marketplace_list")
    def test_url_marketplace_list(self):
        "тест: проверка url marketplace_list"
        url = reverse('product:marketplace_list')
        assert url == '/product/marketplaces/'

    @allure.title("тест: проверка url marketplace_create")
    def test_url_marketplace_create(self):
        "тест: проверка url marketplace_create"
        url = reverse('product:marketplace_create')
        assert url == '/product/marketplace/create/'

    @allure.title("тест: проверка url marketplace_delete")
    def test_url_marketplace_delete(self):
        "тест: проверка url marketplace_delete"
        url = reverse('product:marketplace_delete', kwargs={'pk': 1})
        assert url == '/product/marketplace/1/delete/'
