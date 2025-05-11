import tempfile
import shutil

from django.conf import settings
from django.test import TestCase, override_settings
from django.urls import reverse

from account.models import User

TEMP_MEDIA_ROOT = tempfile.mkdtemp(dir=settings.MEDIA_ROOT_TESTS)


class MarkitingMessagePermissionAdmin(TestCase):
    "Тест кейс проверки доступа от админа связанных с моделью MarkitingMessage"

    @classmethod
    def setUpClass(cls):
        cls.temp_media = tempfile.TemporaryDirectory()
        User.objects.all().delete()
        User.objects.create_superuser(
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
        self.client.force_login(
            username='username',
            password='password'
        )

    def test_marketing_message_list_permmission_admin(self):
        "тест: проверка доступа админа до marketing_message_list"
        response = self.client.get(reverse("telegram:marketing_message_list"))
        self.assertEqual(response.status_code, 200)
