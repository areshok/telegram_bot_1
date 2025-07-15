import allure
from django.urls import reverse


class TestCaseProductPermissionAdminUser:
    "Тест кейс проверки доступа от админа связанных с моделью product"

    @allure.title("тест: проверка доступа админа до post_list")
    def test_post_list_admin_user_access(self, auth_admin):
        "тест: проверка доступа админа до post_list"
        response = auth_admin.get(reverse('product:product_list'))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до post_detail")
    def test_post_detail_admin_user_access(self, auth_admin, product):
        "тест: проверка доступа админа до post_detail"
        response = auth_admin.get(
            reverse("product:product_detail", kwargs={"pk": product.id}))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до product_update")
    def test_product_update_admin_user_access(self, auth_admin, product):
        "тест: проверка доступа админа до product_update"
        response = auth_admin.get(
            reverse('product:product_update', kwargs={'pk': product.id}))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до product_create")
    def test_product_create_admin_user_access(self, auth_admin):
        "тест: проверка доступа админа до product_create"
        response = auth_admin.get(reverse('product:product_create'))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до product_delete")
    def test_product_delete_admin_user_access(self, auth_admin, product):
        "тест: проверка доступа админа до product_delete"
        response = auth_admin.post(
            reverse('product:product_delete',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до qrcode_download")
    def test_qrcode_download_admin_user_access(self, auth_admin, product):
        "тест: проверка доступа админа до qrcode_download"
        response = auth_admin.get(
            reverse('product:qrcode_download', kwargs={'pk': product.id}))
        assert f'qrcode/{product.id}_{product.name}_qrcode' in str(product.qrcode)
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до qrcode_create")
    def test_qrcode_create_admin_user_access(self, auth_admin, product):
        "тест: проверка доступа админа до qrcode_create"
        response = auth_admin.get(
            reverse('product:qrcode_create',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до qrcode_delete")
    def test_qrcode_delete_admin_user_access(self, auth_admin, product):
        "тест: проверка доступа админа до qrcode_delete"
        response = auth_admin.post(
            reverse('product:qrcode_delete',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 200


class TestCaseMarketplacePermissionAdminUser:
    "Тест кейс проверки доступа от админа связанных с моделью marketplace"

    @allure.title("тест: проверка доступа админа до marketplace_list")
    def test_marketplace_list_admin_user_access(self, auth_admin):
        "тест: проверка доступа админа до marketplace_list"
        response = auth_admin.get(reverse('product:marketplace_list'))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до create_marketplace")
    def test_marketplace_create_admin_user_access(self, auth_admin):
        "тест: проверка доступа админа до create_marketplace"
        response = auth_admin.get(reverse('product:marketplace_create'))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа админа до marketplace_delete")
    def test_marketplace_delete_admin_user_access(
        self, auth_admin, marketplace
    ):
        "тест: проверка доступа админа до marketplace_delete"
        response = auth_admin.get(
            reverse('product:marketplace_delete',
                    kwargs={'pk': marketplace.id}), follow=True)
        assert response.status_code == 200
