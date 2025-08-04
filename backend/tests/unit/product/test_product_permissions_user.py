import allure
from django.urls import reverse


class TestCaseProductPermissionAuthUser:
    """
    Тест кейс проверки доступа от авторизированного пользователя
    связанных с моделью product
    """

    @allure.title(
        "тест: проверка доступа авторизированного пользователя до post_list"
    )
    def test_post_list_auth_user_access(self, auth_user):
        "тест: проверка доступа авторизированного пользователя до post_list"
        response = auth_user.get(reverse('product:product_list'))
        assert response.status_code == 200

    @allure.title(
        "тест: проверка доступа авторизированного пользователя до post_detail")
    def test_post_detail_auth_user_access(self, auth_user, product):
        "тест: проверка доступа авторизированного пользователя до post_detail"
        response = auth_user.get(
            reverse("product:product_detail", kwargs={"pk": product.id}))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа авторизированного пользователя до product_update")
    def test_product_update_auth_user_access(self, auth_user, product):
        "тест: проверка доступа авторизированного пользователя до product_update"
        response = auth_user.get(reverse('product:product_update', kwargs={'pk': product.id}))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа авторизированного пользователя до product_create")
    def test_product_create_auth_user_access(self, auth_user):
        "тест: проверка доступа авторизированного пользователя до product_create"
        response = auth_user.get(reverse('product:product_create'))
        assert response.status_code == 200

    @allure.title("тест: проверка доступа авторизированного пользователя до product_delete")
    def test_product_delete_auth_user_access(self, auth_user, product):
        "тест: проверка доступа авторизированного пользователя до product_delete"
        response = auth_user.post(reverse('product:product_delete', kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 200

    @allure.title("тест: проверка доступа авторизированного пользователя до qrcode_download")
    def test_qrcode_download_auth_user_access(self, auth_user, product):
        "тест: проверка доступа авторизированного пользователя до qrcode_download"
        response = auth_user.get(reverse('product:qrcode_download', kwargs={'pk': product.id}))
        assert f'qrcode/{product.id}_{product.name}_qrcode' in str(product.qrcode)
        assert response.status_code == 200

    @allure.title("тест: проверка доступа авторизированного пользователя до qrcode_create")
    def test_qrcode_create_auth_user_access(self, auth_user, product):
        "тест: проверка доступа авторизированного пользователя до qrcode_create"
        response = auth_user.get(reverse('product:qrcode_create', kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 200

    @allure.title("тест: проверка доступа авторизированного пользователя до qrcode_delete")
    def test_qrcode_delete_auth_user_access(self, auth_user, product):
        "тест: проверка доступа авторизированного пользователя до qrcode_delete"
        response = auth_user.post(
            reverse('product:qrcode_delete',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 200


class TestCaseMarketplacePermissionAuthUser:
    "Тест кейс проверки доступа авторизированного пользователя связанных с моделью marketplace"

    @allure.title("тест: проверка доступа авторизированного пользователя до marketplace_list")
    def test_marketplace_list_auth_user_access(self, auth_user):
        "тест: проверка доступа авторизированного пользователя до marketplace_list"
        response = auth_user.get(reverse('product:marketplace_list'))
        assert response.status_code == 403

    @allure.title("тест: проверка доступа авторизированного пользователя до create_marketplace")
    def test_marketplace_create_auth_user_access(self, auth_user):
        "тест: проверка доступа авторизированного пользователя до create_marketplace"
        response = auth_user.get(reverse('product:marketplace_create'))
        assert response.status_code == 403

    @allure.title("тест: проверка доступа авторизированного пользователя до marketplace_delete")
    def test_marketplace_delete_auth_user_access(self, auth_user, marketplace):
        "тест: проверка доступа авторизированного пользователя до marketplace_delete"
        response = auth_user.get(
            reverse('product:marketplace_delete',
                    kwargs={'pk': marketplace.id}), follow=True)
        assert response.status_code == 403
