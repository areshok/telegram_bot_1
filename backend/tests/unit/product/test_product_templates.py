from django.urls import reverse


class TestCaseProductTemplate:

    def test_product_list_template(self, auth_user):
        "тест: проверка шаблона product_list"
        response = auth_user.get(reverse('product:product_list'))
        assert response.status_code == 200
        assert 'product/product_list.html' in [template.name for template in response.templates]

    def test_product_detail_template(self, auth_user, product):
        "тест: проверка шаблона product_detail"
        url = reverse('product:product_detail', kwargs={'pk': product.id})
        response = auth_user.get(url)
        assert response.status_code == 200
        assert 'product/product_detail.html' in [template.name for template in response.templates]

    def test_product_create_template(self, auth_user):
        "тест: проверка шаблона product_create"
        response = auth_user.get(reverse('product:product_create'))
        assert response.status_code == 200
        assert 'product/product_create.html' in [template.name for template in response.templates]

    def test_product_update_template(self, auth_user, product):
        "тест: проверка шаблона product_update"
        response = auth_user.get(
            reverse('product:product_update', kwargs={'pk': product.id})
        )
        assert response.status_code == 200
        assert 'product/product_update.html' in [template.name for template in response.templates]
