from django.test import TestCase
from django.urls import reverse


class MarketingMassageUrlTest(TestCase):
    "Тест кейс првоерки url связанных с моделью MarketingMessage"

    def test_marketing_message_list_url(self):
        "тест: проверка url marketing_message_list"
        url = reverse("telegram:marketing_message_list")
        self.assertEqual(url, "/telegram/marketing-meassage/list/")

    def test_marketing_message_detail_url(self):
        "тест: проверка url marketing_message_detail"
        url = reverse("telegram:marketing_message_detail", kwargs={"pk": 1})
        self.assertEqual(url, "/telegram/markiting-message/1/")

    def test_markiting_message_create_url(self):
        "тест: проверка url marketing_message_create"
        url = reverse("telegram:marketing_message_create")
        self.assertEqual(url, "/telegram/marketing-message/create/")

    def test_markiting_message_update_url(self):
        "тест: проверка url marketing_message_update"
        url = reverse("telegram:marketing_message_update", kwargs={"pk": 1})
        self.assertEqual(url, "/telegram/markiting-message/1/update/")

    def test_markiting_message_delete_url(self):
        "тест: проверка url markiting_message_delete"
        url = reverse("telegram:markiting_message_delete", kwargs={"pk": 1})
        self.assertEqual(url, "/telegram/markiting-message/1/delete/")

    def test_markiting_message_send_url(self):
        "тест: првоерка url markiting_message_send"
        url = reverse("telegram:markiting_message_send", kwargs={"pk": 1})
        self.assertEqual(url, '/telegram/markiting-message/1/send/')


class CommentProductUrlTest(TestCase):
    "Тест кейс проверки url связанных с моделью CommentProduct"

    def test_comment_product_list_url(self):
        "тест: проверка url comment_product_list"
        url = reverse("telegram:comment_product_list")
        self.assertEqual(url, "/telegram/comment/")

    def test_comment_product_detail_url(self):
        "тест: проверка url comment_product_detail"
        url = reverse("telegram:comment_product_detail", kwargs={"pk": 1})
        self.assertEqual(url, "/telegram/comment/1/")

    def test_comment_product_update_url(self):
        "тест: проверка url comment_product_update"
        url = reverse("telegram:comment_product_update", kwargs={"pk": 1})
        self.assertEqual(url, '/telegram/comment/1/update/')
