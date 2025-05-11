import tempfile
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse

from account.models import User

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.MEDIA_ROOT_TESTS)


class MarkitingMessageTemplateTest(TestCase):
    "Тест кейс проверки шаблонов связанных с моделью MarkitingMessage"

    @classmethod
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        User.objects.all().delete()
        User.objects.create_user(
            username='username',
            password='password'
        )
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        return super().tearDownClass()

    def setUp(self):
        self.client.login(
            username='username',
            password='password'
        )

    def test_marketing_message_list_template(self):
        "тест: проверка шаблона marketing_message_list"
        response = self.client.get(reverse("telegram:marketing_message_list"))
        self.assertTemplateUsed(
            response, 'telegram/marketing_message_list.html')

    def test_marketing_message_detail_template(self):
        "тест: проверка шаблона marketing_message_detail"
        response = self.client.get(
            reverse("telegram:marketing_message_detail",  kwargs={"pk": 1}))
        self.assertTemplateUsed(
            response, 'telegram/marketing_message_detail.html')

    def test_markiting_message_create_template(self):
        "тест: проверка шаблона markiting_message_create"
        response = self.client.get(
            reverse("telegram:markiting_message_create"))
        self.assertTemplateUsed(
            response, "telegram/markiting_message_create.html")

    def test_markiting_message_update_template(self):
        "тест: проверка шаблона markiting_message_update"
        response = self.client.get(
            reverse("telegram:markiting_message_update", kwargs={"pk": 1}))
        self.assertTemplateUsed(
            response, "telegram/markiting_message_create.html")


class CommentProductTemplateTest(TestCase):
    "Тест кейс првоерки  шаблонов связанных с моделью CommentProduct"

    @classmethod
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        User.objects.all().delete()
        User.objects.create_user(
            username='username',
            password='password'
        )
        return super().setUpClass()

    @classmethod
    def tearDownClass(cls):
        User.objects.all().delete()
        shutil.rmtree(TEMP_MEDIA_ROOT, ignore_errors=True)
        return super().tearDownClass()

    def setUp(self):
        self.client.login(
            username='username',
            password='password'
        )

    def test_comment_product_list_template(self):
        "тест: проверка шаблона comment_product_list"
        response = self.client.get(reverse("telegram:comment_product_list"))
        self.assertTemplateUsed(response, "telegram/comment_product_list.html")

    def test_comment_product_detail_template(self):
        "тест: проверка щаблона comment_product_detail"
        response = self.client.get(
            reverse("telegram:comment_product_detail", kwargs={"pk": 1}))
        self.assertTemplateUsed(
            response, "telegram/comment_product_detail.html")

    def test_comment_product_update_template(self):
        "тест: проверка шаблона comment_product_update"
        response = self.client.get(
            reverse("telegram:comment_product_update", kwargs={"pk": 1}))
        self.assertTemplateUsed(response, "telegram/comment_product_update.html")
