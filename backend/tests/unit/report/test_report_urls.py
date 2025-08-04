from django.urls import reverse


class TestCaseReportUrl:
    "Тест кейс проверки url связанных с отчетами"

    def test_report_comment_url(self):
        "тест: проверка url report_comment"
        url = reverse("report:report_comment")
        assert url == '/report/comment/'

    def test_report_review_of_comments_url(self):
        "тест: проверка url report_review_comment"
        url = reverse("report:report_review_comment")
        assert url == "/report/user-review/"

    def test_report_product_url_url(self):
        "тест: проверка url report_product_url"
        url = reverse("report:report_product_url")
        assert url == '/report/product-url'

    def test_report_maketing_message_url(self):
        "тест: проверка url report_marketing_message"
        url = reverse("report:report_marketing_message")
        assert url == '/report/marketing-message/'
