from django.test import TestCase
from django.urls import reverse


class ReportUrlTest(TestCase):
    "Тест кейс проверки url связанных с отчетами"

    def test_report_comment_url(self):
        "тест: проверка url report_comment"
        url = reverse("report:report_comment")
        self.assertEqual(url, '/report/comment/')

    def test_report_review_of_comments_url(self):
        "тест: проверка url report_review_comment"
        url = reverse("report:report_review_comment")
        self.assertEqual(url, "/report/user-review/")

    def test_report_product_url_url(self):
        "тест: проверка url report_product_url"
        url = reverse("report:report_product_url")
        self.assertEqual(url, '/report/product-url')

    def test_report_maketing_message_url(self):
        "тест: проверка url report_marketing_message"
        url = reverse("report:report_marketing_message")
        self.assertEqual(url, '/report/marketing-message/')
