import allure

from django.urls import reverse


class TestCaseProductPermissionAnonUser:
    "Тест кейс проверки доступа от анонимного пользователя связанных с моделью product"

    @allure.title("тест: проверка доступа анонимного пользователя до post_list")
    @allure.description("Переадресация на странцу входа")
    def test_post_list_anonim_user_access(self, anon_user):
        "тест: проверка доступа анонимного пользователя до post_list"
        response = anon_user.get(reverse('product:product_list'))
        assert response.status_code == 302
        assert reverse("account:login") in response.url


    @allure.title("тест: проверка доступа анонимного пользователя до post_detail")
    @allure.description("Переадресация на странцу входа")
    def test_post_detail_anonim_user_access(self, anon_user, product):
        "тест: проверка доступа анонимного пользователя до post_detail"
        response = anon_user.get(
            reverse("product:product_detail", kwargs={"pk": product.id}))
        assert response.status_code == 302
        assert reverse("account:login") in response.url

    @allure.title("тест: проверка доступа анонимного пользователя до product_update")
    @allure.description("Переадресация на странцу входа")
    def test_product_update_anonim_user_access(self, anon_user, product):
        "тест: проверка доступа анонимного пользователя до product_update"
        response = anon_user.get(
            reverse('product:product_update', kwargs={'pk': product.id}))
        assert response.status_code == 302
        assert reverse("account:login") in response.url

    @allure.title("тест: проверка доступа анонимного пользователя до product_create")
    @allure.description("Переадресация на странцу входа")
    def test_product_create_anonim_user_access(self, anon_user):
        "тест: проверка доступа анонимного пользователя до product_create"
        response = anon_user.get(reverse('product:product_create'))
        assert response.status_code == 302
        assert reverse("account:login") in response.url

    @allure.title("тест: проверка доступа анонимного пользователя до product_delete")
    @allure.description("Переадресация на странцу входа")
    def test_product_delete_anonim_user_access(self, anon_user, product):
        "тест: проверка доступа анонимного пользователя до product_delete"
        response = anon_user.post(
            reverse('product:product_delete',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 302
        assert reverse("account:login") in response.url

    @allure.title("тест: проверка доступа анонимного пользователя до qrcode_download")
    @allure.description("Переадресация на странцу входа")
    def test_qrcode_download_anonim_user_access(self, anon_user, product):
        "тест: проверка доступа анонимного пользователя до qrcode_download"
        response = anon_user.get(
            reverse('product:qrcode_download', kwargs={'pk': product.id}))
        assert f'qrcode/{product.id}_{product.name}_qrcode' in str(product.qrcode)
        assert response.status_code == 302
        assert reverse("account:login") in response.url

    @allure.title("тест: проверка доступа анонимного пользователя до qrcode_create")
    @allure.description("Переадресация на странцу входа")
    def test_qrcode_create_anonim_user_access(self, anon_user, product):
        "тест: проверка доступа анонимного пользователя до qrcode_create"
        response = anon_user.get(
            reverse('product:qrcode_create',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 302
        assert reverse("account:login") in response.url

    @allure.title("тест: проверка доступа анонимного пользователя до qrcode_delete")
    @allure.description("Переадресация на странцу входа")
    def test_qrcode_delete_anonim_user_access(self, anon_user, product):
        "тест: проверка доступа анонимного пользователя до qrcode_delete"
        response = anon_user.post(
            reverse('product:qrcode_delete',
                    kwargs={'pk': product.id}), follow=True)
        assert response.status_code == 302
        assert reverse("account:login") in response.url


class TestCaseMarketplacePermissionAnonUser:
    "Тест кейс проверки доступа анонимного пользователя связанных с моделью marketplace"

    @allure.title("тест: проверка доступа анонимного пользователя до marketplace_list")
    @allure.description("Доступ запрещен")
    def test_marketplace_list_anon_user_access(self, anon_user):
        "тест: проверка доступа анонимного пользователя до marketplace_list"
        response = anon_user.get(reverse('product:marketplace_list'))
        assert response.status_code == 403

    @allure.title("тест: проверка доступа анонимного пользователя до create_marketplace")
    @allure.description("Доступ запрещен")
    def test_marketplace_create_anon_user_access(self, anon_user):
        "тест: проверка доступа анонимного пользователя до create_marketplace"
        response = anon_user.get(reverse('product:marketplace_create'))
        assert response.status_code == 403

    @allure.title("тест: проверка доступа анонимного пользователя до marketplace_delete")
    @allure.description("Доступ запрещен")
    def test_marketplace_delete_anon_user_access(self, anon_user, marketplace):
        "тест: проверка доступа анонимного пользователя до marketplace_delete"
        response = anon_user.get(
            reverse('product:marketplace_delete',
                    kwargs={'pk': marketplace.id}), follow=True)
        assert response.status_code == 403
