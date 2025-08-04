import tempfile
import shutil

import allure
from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse

from account.models import User

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.MEDIA_ROOT_TESTS)


class TestCaseMarkitingMessageTemplate:
    "Тест кейс проверки используемости шаблонов шаблонов модели MarketingMessage"

    @allure.title("тест: проверка шаблона marketing_message_list")
    def test_marketing_message_list_template(self, admin_client):
        "тест: проверка шаблона marketing_message_list"
        response = admin_client.get(reverse("telegram:marketing_message_list"))
        assert 'telegram/marketing_message_list.html' in \
            [template.name for template in response.templates]

    @allure.title("тест: проверка шаблона marketing_message_detail")
    def test_marketing_message_detail_template(self, admin_client):
        "тест: проверка шаблона marketing_message_detail"
        response = admin_client.get(
            reverse("telegram:marketing_message_detail",  kwargs={"pk": 1}))
        assert 'telegram/marketing_message_detail.html' in \
            [template.name for template in response.templates]

    @allure.title("тест: проверка шаблона markiting_message_create")
    def test_markiting_message_create_template(self, admin_client):
        "тест: проверка шаблона markiting_message_create"
        response = admin_client.get(
            reverse("telegram:markiting_message_create"))
        assert "telegram/markiting_message_create.html" in \
            [template.name for template in response.templates]

    @allure.title("тест: проверка шаблона markiting_message_update")
    def test_markiting_message_update_template(self, admin_client):
        "тест: проверка шаблона markiting_message_update"
        response = admin_client.get(
            reverse("telegram:markiting_message_update", kwargs={"pk": 1}))
        assert response.status_code == 200
        assert "telegram/markiting_message_create.html" in \
            [template.name for template in response.templates]


class TestCaseTelegramProfileTemplate:
    ""

    def test_():
        assert 1 == 2


class TestCaseCommentProductTemplate:
    "Тест кейс проверки используемости шаблонов шаблонов модели CommentProduct"

    @allure.title("тест: проверка шаблона product_comment_list")
    def test_comment_product_list_template(self, admin_client):
        "тест: проверка шаблона product_comment_list"
        response = admin_client.get(reverse("telegram:comment_product_list"))
        assert response.status_code == 200
        assert "telegram/comment_product_list.html" in \
            [template.name for template in response.templates]

    @allure.title("тест: проверка шаблона comment_product_detail")
    def test_comment_product_detail_template(self, admin_client, comment_product):
        "тест: проверка шаблона comment_product_detail"
        response = admin_client.get(reverse("telegram:comment_product_detail", kwargs={"pk": comment_product.id}))
        assert response.status_code == 200
        assert "telegram/comment_product_detail.html" in \
            [template.name for template in response.templates]

    @allure.title("тест: проверка шаблона comment_product_update")
    def test_comment_product_update(self, admin_client, comment_product):
        "тест: проверка шаблона comment_product_update"
        response = admin_client.post(reverse("telegram:comment_product_update", kwargs={"pk": comment_product.id}))
        assert response.status_code == 200
        assert "telegram/comment_product_update.html" in \
            [template.name for template in response.templates]
